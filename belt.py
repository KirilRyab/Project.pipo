from product import Product

class Belt(Product):
    def __init__(self, product_id, forms_available, rubber_type, cord_type, jacket_type, belt_width):
        super().__init__(product_id, forms_available, rubber_type, cord_type, jacket_type)
        self._belt_width = belt_width

    @property
    def belt_width(self):
        return self._belt_width

    def calculate_resource_usage(self, quantity):
        return {"rubber": quantity * 1, "cord": quantity * 0.5, "jacket": quantity * 0.2}
