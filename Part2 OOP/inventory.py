class Inventory:
    def __init__(self):
        self.__inventory = []

    def add_product(self, product) -> bool:
        if self.find_product(product.get_product_id()) is not None:
            return False  # duplicate ID
        self.__inventory.append(product)
        return True

    def find_product(self, product_id: str):
        for product in self.__inventory:
            if product.get_product_id().lower() == product_id.lower():
                return product
        return None

    def update_stock(self, product_id: str, quantity: int) -> bool:
        product = self.find_product(product_id)
        if product is None:
            return False
        return product.update_stock(quantity)

    def search_product(self, search: str):
        found = False
        for product in self.__inventory:
            if (search.lower() in product.get_name().lower()
                    or search.lower() in product.get_product_id().lower()):
                product.display_information()
                found = True

        if not found:
            print(f"No products found matching '{search}'.\n")

    def display_all(self):
        if not self.__inventory:
            print("Inventory is empty.")
        for product in self.__inventory:
            product.display_information()

    def get_products(self) -> list:
        return list(self.__inventory)
