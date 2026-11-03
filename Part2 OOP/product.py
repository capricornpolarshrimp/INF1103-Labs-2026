class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def update_stock(self, quantity: int) -> bool:
        # Product controls its own state: stock can never go below 0
        if self.__stock + quantity < 0:
            return False
        self.__stock += quantity
        return True

    def display_information(self):
        print(f"\nProduct ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    def to_dict(self) -> dict:
        # lets main.py save this product to JSON without touching private attributes
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }
