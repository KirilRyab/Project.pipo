from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, forms_available, rubber_type, cord_type, jacket_type):
        self._product_id = product_id
        self._forms_available = forms_available
        self._rubber_type = rubber_type
        self._cord_type = cord_type
        self._jacket_type = jacket_type

    @property
    def product_id(self):
        return self._product_id

    @property
    def forms_available(self):
        return self._forms_available

    @property
    def rubber_type(self):
        return self._rubber_type

    @property
    def cord_type(self):
        return self._cord_type

    @property
    def jacket_type(self):
        return self._jacket_type

    @abstractmethod
    def calculate_resource_usage(self, quantity):
        pass
    
