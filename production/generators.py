import random
import pandas as pd
from datetime import datetime, timedelta
from models import Product, SpecialProduct, Order

class ProductGenerator:

    def __init__(self, count=10):
        self.count = count

    def generate_products(self):
        product_list = []
        for _ in range(self.count):
            p1 = str(random.randint(1000, 9999))
            p2 = str(random.randint(10000, 99999))
            pid = f"{p1}-{p2}"
            fc = random.randint(1, 4)
            bpf = random.randint(25, 40)

            is_special = (lambda: random.random() < 0.2)()

            if is_special:
                product_obj = SpecialProduct(pid, fc, bpf, premium=True)
            else:
                product_obj = Product(pid, fc, bpf)

            product_list.append(product_obj)
        return product_list


def generate_products_csv(file_path: str, num_products: int = 10):

    gen = ProductGenerator(count=num_products)
    products = gen.generate_products()
    data = []
    for p in products:
        data.append({
            "product_id": p.product_id,
            "form_count": p.form_count,
            "belts_per_form": p.belts_per_form
        })
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"[INFO] Products saved to {file_path}")


def generate_orders_csv(file_path: str, product_file_path: str, num_orders: int = 5):
    df_products = pd.read_csv(product_file_path)
    if df_products.empty:
        print("[WARNING] No products to generate orders.")
        return

    def random_deadline():

        days = random.randint(1, 15)
        return datetime.today() + timedelta(days=days)

    orders_list = []
    for _ in range(num_orders):
        row = df_products.sample(1).iloc[0]
        pid = row["product_id"]
        quantity = random.randint(2000, 10000)

        dl = (lambda: random_deadline())()
        orders_list.append({
            "order_id": str(random.randint(100000, 999999)),
            "product_id": pid,
            "quantity": quantity,
            "deadline": dl.date()
        })

    df_o = pd.DataFrame(orders_list)
    df_o.to_csv(file_path, index=False)
    print(f"[INFO] Orders saved to {file_path}")
