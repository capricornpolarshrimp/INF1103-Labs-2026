inventory = 0
failed_attempts = 0

def get_valid_input():
    while True:
        user_input = input("Enter Stock Quantity (or 'quit' to stop): ").strip()

        if user_input.lower() == "quit":
            return "quit"

        if user_input.isdigit():
            return int(user_input)

        print("Error: Input must be a positive integer.")
        return None

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

# Main Loop
while inventory <= 500:
    stock_input = get_valid_input()

    # Handle quit command
    if stock_input == "quit":
        generate_report(inventory, failed_attempts)
        break

    # Handle failed validation
    if stock_input is None:
        failed_attempts += 1
        continue

    # Process valid stock delivery
    tax = calculate_tax(stock_input)
    inventory = process_delivery(inventory, stock_input)
    print(f"Delivery processed: {stock_input} units (Tax applied: {tax})")

# Check for overstock condition
if inventory > 500:
    print("Overstock Alert > 500")
    generate_report(inventory, failed_attempts)