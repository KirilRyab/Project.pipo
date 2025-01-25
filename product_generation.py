import pandas as pd
import random

class ProductGenerator:
    @staticmethod
    def generate(output_file, num_products):
        products = []
        for i in range(num_products):
            product_id = f"{random.randint(1000, 9999)}-{random.randint(10000, 99999)}"
            belt_width = random.uniform(20, 40)  # Random belt width between 20mm and 40mm
            forms_available = random.randint(1, 4)  # Random number of available forms (1-4)
            slab_width = 1020  # Default slab width (fixed for all products)
            rubber_type = random.choice(["A", "B", "C"])  # Random rubber type
            cord_type = random.choice(["X", "Y", "Z"])  # Random cord type
            jacket_type = random.choice(["P", "Q", "R"])  # Random jacket type

            products.append({
                "product_id": product_id,
                "belt_width": belt_width,
                "forms_available": forms_available,
                "slab_width": slab_width,
                "rubber_type": rubber_type,
                "cord_type": cord_type,
                "jacket_type": jacket_type
            })

        products_df = pd.DataFrame(products)
        products_df.to_csv(output_file, index=False)
        print(f"Products table saved to '{output_file}'.")
