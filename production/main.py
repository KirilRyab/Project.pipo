from generators import generate_products_csv, generate_orders_csv
from production_plan import WeeklyPlanner, PlanOverflowError

def main():
    print("Starting main...")

    print("Generating products ...")
    generate_products_csv("product_table.csv", num_products=10)

    print("Generating orders ...")
    generate_orders_csv("order_table.csv", "product_table.csv", num_orders=8)

    print("Scheduling production with WeeklyPlanner...")
    planner = WeeklyPlanner(num_kettles=12, max_cycles_per_shift=11, shifts_per_day=3, days_per_week=5)

    try:
        planner.plan("order_table.csv", "product_table.csv")
    except PlanOverflowError as e:
        print("OverFlow", str(e))
    except Exception as e:
        print("Unexpected error:", e)

    print("Done.")

if __name__ == "__main__":
    main()
