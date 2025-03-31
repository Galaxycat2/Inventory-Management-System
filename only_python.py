#Inventory management system using only Python 
inventory = {}

def add_item():
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    inventory[item_name] = inventory.get(item_name, 0) + quantity
    print(f"{quantity} {item_name}(s) added to inventory.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("Current Inventory:")
    for item_name, quantity in inventory.items():
        print(f"- {item_name}: {quantity}")

def update_item():
    item_name = input("Enter item name to update: ")
    if item_name not in inventory:
        print("Item not found in inventory.")
        return
    new_quantity = int(input(f"Enter new quantity for {item_name}: "))
    inventory[item_name] = new_quantity
    print(f"{item_name} quantity updated to {new_quantity}.")

def remove_item():
    item_name = input("Enter item name to remove: ")
    if item_name not in inventory:
        print("Item not found in inventory.")
        return
    quantity_to_remove = int(input(f"Enter quantity to remove from {item_name}: "))
    if quantity_to_remove > inventory[item_name]:
        print("Not enough items in stock.")
        return
    inventory[item_name] -= quantity_to_remove
    if inventory[item_name] == 0:
        del inventory[item_name]
    print(f"{quantity_to_remove} {item_name}(s) removed from inventory.")

while True:
    print("\nInventory Management System")
    print("1. Add item")
    print("2. View inventory")
    print("3. Update item")
    print("4. Remove item")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        view_inventory()
    elif choice == '3':
        update_item()
    elif choice == '4':
        remove_item()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")