from product import Product

class Slab(Product):
    def __init__(self, product_id, forms_available, rubber_type, cord_type, jacket_type, slab_width):
        super().__init__(product_id, forms_available, rubber_type, cord_type, jacket_type)
        self._slab_width = slab_width

    @property
    def slab_width(self):
        return self._slab_width

    def calculate_belts(self, belt_width):
        return int(self.slab_width / belt_width)

    def calculate_resource_usage(self, quantity):
        return {"rubber": quantity * 2, "cord": quantity * 1.5, "jacket": quantity * 1}
    
