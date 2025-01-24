from abc import ABC, abstractmethod

class QuantityError(Exception):
    pass

class AbstractItem(ABC):
    @abstractmethod
    def info(self) -> str:
        pass

class ProductionCapable(ABC):
    @abstractmethod
    def produce(self, cycles: int) -> None:
        pass

class Product(AbstractItem, ProductionCapable):
    def __init__(self, product_id: str, form_count: int, belts_per_form: int):
        self._product_id = product_id
        self._form_count = form_count
        self._belts_per_form = belts_per_form

    @property
    def product_id(self) -> str:
        return self._product_id

    @property
    def form_count(self) -> int:
        return self._form_count

    @property
    def belts_per_form(self) -> int:
        return self._belts_per_form

    def info(self) -> str:
        return (f"Product({self.product_id}), forms={self.form_count}, "
                f"bpf={self.belts_per_form}")

    def produce(self, cycles: int) -> None:
        if cycles < 0:
            raise QuantityError("Cannot produce negative cycles.")
        pass
        



class SpecialProduct(Product):  
    def __init__(self, product_id: str, form_count: int, belts_per_form: int, premium: bool):
        super().__init__(product_id, form_count, belts_per_form)
        self._premium = premium

    def info(self) -> str:
        basic = super().info()
        return basic + (", Premium" if self._premium else ", Standard")

class Order:
    def __init__(self, order_id: str, product: Product, belts_needed: int):
        if belts_needed <= 0:
            raise QuantityError("Order must have positive belt quantity.")
        self.order_id = order_id
        self.product = product
        self.belts_needed = belts_needed

    def __str__(self) -> str:
        return f"Order[{self.order_id}] -> {self.product.product_id}, belts={self.belts_needed}"
