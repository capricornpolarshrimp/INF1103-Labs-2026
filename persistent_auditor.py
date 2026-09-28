import os

filename = "inventory.txt"
orders = []
inventory = 0
failed_attempts = 0
next_order_id = 1001

def load_inventory():
    global inventory, orders, next_order_id
    if os.path.exists(filename):
        print("Current Orders:")
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) == 3:
                    order_id = int(parts[0].strip())
                    name = parts[1].strip()
                    qty = int(parts[2].strip())
                orders.append((order_id, name, qty))
                inventory += qty
                print(f"{order_id}, {name}, {qty}")
    if orders:
            next_order_id = max(order[0] for order in orders) + 1
    else:
        print(f"No existing '{filename}' found")

def save_inventory():
    with open(filename, "w") as file:
        for order_id, name, qty in orders:
            file.write(f"{order_id}, {name}, {qty}\n")
    print(f"Order successfully saved to {filename}")



def get_valid_input():
    while True:
        name_input = input("Enter Product Name: ").strip()

        if name_input.lower() == "quit":
            return "quit", None

        qty_input = input("Enter Quantity: ").strip()

        if qty_input.isdigit():
            return name_input, int(qty_input)
        else:
            print("Error: Input must be a positive integer.")
            return None, None

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

load_inventory()

# Main Loop
while inventory <= 500:
    product_name, qty = get_valid_input()

    # Handle quit command
    if product_name == "quit":
        save_inventory()
        generate_report(inventory, failed_attempts)
        break

    # Handle failed validation
    if product_name is None or qty is None:
        failed_attempts += 1
        continue

    # Process valid stock delivery
    tax = calculate_tax(qty)
    inventory = process_delivery(inventory, qty)

    orders.append((next_order_id, product_name, qty))
    print(f"\nNew Order Added:\n{next_order_id}, {product_name}, {qty}")
    next_order_id += 1

    save_inventory()

# Check for overstock condition
if inventory > 500:
    print("Overstock Alert > 500")
    generate_report(inventory, failed_attempts)