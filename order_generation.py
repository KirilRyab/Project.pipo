
import pandas as pd
import random

class OrderGenerator:
    @staticmethod
    def generate(input_products_file, output_orders_file, num_orders):
        products_df = pd.read_csv(input_products_file)
        orders = []
        order_id = 1

        for _ in range(num_orders):
            product = products_df.sample().iloc[0]
            belt_quantity = random.randint(500, 5000)  # Random belt quantity
            orders.append({
                "order_id": f"{order_id:06d}",
                "product_id": product["product_id"],
                "belt_quantity": belt_quantity,
                "deadline": random.randint(1, 30)  # Random deadline within the month
            })
            order_id += 1

        orders_df = pd.DataFrame(orders)
        orders_df.to_csv(output_orders_file, index=False)
        print(f"Orders table saved to '{output_orders_file}'.")
