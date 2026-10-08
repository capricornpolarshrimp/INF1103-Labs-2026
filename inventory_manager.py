inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
]


def display_all(inventory):
    print("\nCurrent Inventory")
    print("-" * 48)
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print("-" * 48)


def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    inventory.append({"id": product_id, "name": name, "price": price, "stock": stock})
    print("Product added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    for p in inventory:
        if p["id"] == product_id:
            print("Product Found:")
            print("Name:", p["name"])
            print("Current Stock:", p["stock"])
            p["stock"] = int(input("New Stock Quantity: "))
            print("Stock updated successfully!")
            return
    print("Product not found.")


def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    for p in inventory:
        if p["id"] == product_id:
            print("Product Found")
            print("-" * 48)
            print("ID:", p["id"])
            print("Name:", p["name"])
            print(f"Price: ${p['price']:.2f}")
            print("Stock:", p["stock"])
            print("-" * 48)
            return
    print("Product not found.")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")
        choice = input("Enter option: ")

        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            print("Save not implemented yet.")
        elif choice == "6":
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option.")


main()