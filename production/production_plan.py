import math
import pandas as pd
from abc import ABC, abstractmethod
from models import Order, Product, ProductionCapable
from models import QuantityError


class PlanOverflowError(Exception):
     pass

class IPlanner(ABC):
    @abstractmethod
    def plan(self, orders_csv: str, products_csv: str) -> None:
        pass


class WeeklyPlanner(IPlanner):

    def __init__(
        self,
        num_kettles=12,
        max_cycles_per_shift=11,
        shifts_per_day=3,
        days_per_week=5
    ):

        self.num_kettles = num_kettles
        self.max_cycles_per_shift = max_cycles_per_shift
        self.shifts_per_day = shifts_per_day
        self.days_per_week = days_per_week
        self.schedule = []

    def plan(self, orders_csv: str, products_csv: str) -> None:
        df_orders = pd.read_csv(orders_csv)
        df_orders["deadline"] = pd.to_datetime(df_orders["deadline"])
        df_orders.sort_values("deadline", inplace=True)

        df_products = pd.read_csv(products_csv)
        products_dict = {}
        for _, row in df_products.iterrows():
            pid = row["product_id"]
            p = Product(pid, row["form_count"], row["belts_per_form"])
            products_dict[pid] = p

        orders_list = []
        for _, row in df_orders.iterrows():
            pid = row["product_id"]
            product_obj = products_dict[pid]
            quantity = int(row["quantity"])
            orders_list.append({
                "order_id": row["order_id"],
                "product": product_obj,
                "cycles_needed": math.ceil(quantity / product_obj.belts_per_form)
            })

        day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        total_shifts = self.days_per_week * self.shifts_per_day

        def all_done():
            return all(o["cycles_needed"] <= 0 for o in orders_list)

        current_shift_index = 0
        while not all_done():
            if current_shift_index > 100000:
                raise PlanOverflowError("Too many shifts - overflow scheduling")

            w_index = current_shift_index // total_shifts
            shift_in_week = current_shift_index % total_shifts
            day_of_week = shift_in_week // self.shifts_per_day
            shift_num = (shift_in_week % self.shifts_per_day) + 1
            day_name = day_names[day_of_week]

            kettle_usage = [0]*self.num_kettles

            while True:
                changed = False
                for od in orders_list:
                    if od["cycles_needed"] <= 0:
                        continue
                    product_obj = od["product"]
                    fc = product_obj.form_count
                    free_kettles = [k for k in range(self.num_kettles)
                                    if kettle_usage[k] < self.max_cycles_per_shift]
                    if not free_kettles:
                        break

                    can_use = min(fc, len(free_kettles))
                    assigned = 0
                    for kt in free_kettles:
                        if assigned >= can_use:
                            break
                        used = kettle_usage[kt]
                        cap = self.max_cycles_per_shift - used
                        if cap <= 0:
                            continue
                        need = od["cycles_needed"]
                        to_assign = min(cap, need)
                        if to_assign > 0:
                            try:
                                product_obj.produce(to_assign)
                            except QuantityError as e:
                                print("[ERROR in produce()]", e)
                            self.schedule.append({
                                "week_index": w_index,
                                "day": day_name,
                                "shift": shift_num,
                                "kettle": kt+1,
                                "product_id": product_obj.product_id,
                                "cycles": to_assign
                            })
                            kettle_usage[kt] += to_assign
                            od["cycles_needed"] -= to_assign
                            assigned += 1
                            changed = True
                            if od["cycles_needed"] <= 0:
                                break
                if not changed:
                    break

            current_shift_index += 1
        self._save_by_weeks()

    def _save_by_weeks(self):
        if not self.schedule:
            print("[INFO] No schedule to save.")
            return
        df = pd.DataFrame(self.schedule)
        df["day_shift"] = df["day"] + "_" + df["shift"].astype(str)
        max_week = df["week_index"].max()
        day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        all_shifts = []
        for d in day_names:
            for s in range(1, self.shifts_per_day+1):
                all_shifts.append(f"{d}_{s}")

        for w in range(max_week + 1):
            df_w = df[df["week_index"] == w].copy()
            if df_w.empty:
                continue
            pivot = df_w.pivot_table(
                index=["kettle","product_id"],
                columns="day_shift",
                values="cycles",
                aggfunc="sum",
                fill_value=0
            )
            pivot = pivot.reindex(columns=all_shifts, fill_value=0)
            pivot = pivot.reset_index()
            shifts_map = {col: i for i, col in enumerate(all_shifts)}
            def earliest_shift_index(row):
                mn = 999999
                for c, idx in shifts_map.items():
                    if row[c] != 0 and idx < mn:
                        mn = idx
                return mn
            pivot["first_shift_idx"] = pivot.apply(earliest_shift_index, axis=1)
            pivot.sort_values(["kettle","first_shift_idx","product_id"], inplace=True)
            pivot.drop(columns=["first_shift_idx"], inplace=True)

            pivot.set_index(["kettle","product_id"], inplace=True)
            pivot = pivot[pivot.sum(axis=1) != 0]
            if pivot.empty:
                continue
            fname = f"production_plan_week{w}.csv"
            pivot.to_csv(fname)
            print(f"[INFO] Plan for week {w} saved to {fname}")
