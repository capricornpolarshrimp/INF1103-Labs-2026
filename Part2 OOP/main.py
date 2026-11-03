import json
from inventory import Inventory
from product import Product

FILENAME = "inventory.json"


# ---------- File handling ----------
def save_inventory(inventory: Inventory):
    data = [product.to_dict() for product in inventory.get_products()]
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Inventory saved to {FILENAME}.")


def load_inventory(inventory: Inventory):
    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)
        for item in data:
            inventory.add_product(
                Product(item["product_id"], item["name"], item["price"], item["stock"])
            )
        print(f"Loaded {len(data)} product(s) from {FILENAME}.")
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        print("No valid saved inventory found. Starting with default products.")
        inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
        inventory.add_product(Product("P002", "Mouse", 25.50, 40))
        inventory.add_product(Product("P003", "Wireless Keyboard", 45.00, 25))


# ---------- Menu / UI ----------
def main():
    inventory = Inventory()
    load_inventory(inventory)

    while True:
        print("\n---------- MENU ----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")
        choice = input("Enter option: ")

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            product_id = input("Product ID: ").strip()
            name = input("Name: ").strip()
            try:
                price = float(input("Price: "))
                stock = int(input("Stock: "))
            except ValueError:
                print("Invalid price or stock. Product not added.")
                continue
            if price < 0 or stock < 0:
                print("Price and stock cannot be negative.")
                continue
            if inventory.add_product(Product(product_id, name, price, stock)):
                print(f"Product '{name}' added.")
            else:
                print(f"A product with ID '{product_id}' already exists.")

        elif choice == "3":
            product_id = input("Product ID: ").strip()
            try:
                quantity = int(input("Quantity (positive to restock, negative to sell): "))
            except ValueError:
                print("Invalid quantity.")
                continue
            if inventory.update_stock(product_id, quantity):
                print("Stock updated.")
            else:
                print("Update failed: product not found or not enough stock.")

        elif choice == "4":
            search = input("Search by name or ID: ").strip()
            inventory.search_product(search)

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option.")


main()
