# Snack Inventory
inventory = []

# Sales Record
sales_record = []

# Function to display menu and get user choice
def display_menu():
    print("===== Snack Inventory Management =====")
    print("1. Add a Snack")
    print("2. Update a Snack")
    print("3. Delete a Snack")
    print("4. Sell a Snack")
    print("5. Display Snack Inventory")
    print("6. Display Sales Record")
    print("7. Exit")
    print("======================================")

    choice = input("Enter your choice (1-7): ")
    return choice

# Function to add a snack
def add_snack():
    try:
        name = input("Enter the name of the snack: ")
        id = input("Enter the ID of the snack: ")
        price = float(input("Enter the price of the snack: "))
        availability = int(input("Enter the availability of the snack: "))

        for snack in inventory:
            if snack['id'] == id:
                print("This ID already exists. Please provide a unique ID.")
                return

        snack = {
            'name': name,
            'id': id,
            'price': price,
            'availability': availability
        }
        inventory.append(snack)
        print("Snack added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid value.")

# Function to update a snack
def update_snack():
    try:
        snack_id = input("Enter the ID of the snack to update: ")

        for snack in inventory:
            if snack['id'] == snack_id:
                new_name = input("Enter the new name of the snack: ")
                new_price = float(input("Enter the new price of the snack: "))
                new_availability = int(input("Enter the new availability of the snack: "))

                snack['name'] = new_name
                snack['price'] = new_price
                snack['availability'] = new_availability

                print("Snack updated successfully.")
                return

        print("Invalid snack ID.")
    except ValueError:
        print("Invalid input. Please enter a valid value.")

# Function to delete a snack
def delete_snack():
    try:
        snack_id = input("Enter the ID of the snack to delete: ")

        for snack in inventory:
            if snack['id'] == snack_id:
                inventory.remove(snack)
                print("Snack deleted successfully.")
                return

        print("Invalid snack ID.")
    except ValueError:
        print("Invalid input. Please enter a valid value.")

# Function to sell a snack
def sell_snack():
    try:
        snack_id = input("Enter the ID of the snack to sell: ")

        for snack in inventory:
            if snack['id'] == snack_id:
                if snack['availability'] > 0:
                    snack['availability'] -= 1
                    sales_record.append(snack)
                    print("Snack sold successfully.")
                else:
                    print("This snack is not available.")
                return

        print("Invalid snack ID.")
    except ValueError:
        print("Invalid input. Please enter a valid value.")

# Function to display snack inventory
def display_inventory():
    if inventory:
        print("===== Snack Inventory =====")
        for snack in inventory:
            print(f"Name: {snack['name']}, ID: {snack['id']}, Price: ${snack['price']}, Availability: {snack['availability']}")
    else:
        print("No snacks in the inventory.")

# Function to display sales record
def display_sales_record():
    if sales_record:
        print("===== Sales Record =====")
        for snack in sales_record:
            print(f"Name: {snack['name']}, ID: {snack['id']}, Price: ${snack['price']}")
    else:
        print("No snacks sold.")

# Main program loop
while True:
    choice = display_menu()

    if choice == '1':
        add_snack()
    elif choice == '2':
        update_snack()
    elif choice == '3':
        delete_snack()
    elif choice == '4':
        sell_snack()
    elif choice == '5':
        display_inventory()
    elif choice == '6':
        display_sales_record()
    elif choice == '7':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

    print()  # Print a newline for better readability
