inventory = 0
failed_entry = 0

while inventory <= 500:
    stock_input = input("Enter Stock Quantity: ")

    # Check for quit command
    if stock_input.lower() == "quit":
        print("Total Units Processed:", inventory)
        print("Number of Failed/Rejected Entries:", failed_entry)
        break

    # Check if positive integer
    elif stock_input.isdigit():
        stock_quantity = int(stock_input)
        inventory += stock_quantity
    else:
        print("Error: should be integer")
        failed_entry += 1

# Check for overstock condition
if inventory > 500:
    print("Overstock Alert > 500")
    print("Total Units Processed:", inventory)
    print("Number of Failed/Rejected Entries:", failed_entry)

