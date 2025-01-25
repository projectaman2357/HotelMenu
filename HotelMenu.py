# Define the menu of the restaurant
menu = {
    'pizza': 50,
    'pasta': 40,
    'burger': 60,
    'salad': 70,
    'coffee': 90,  # Fixed spelling from 'cofee' to 'coffee'
}

# Greet the customer
print("Welcome to Python Restaurant!")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: Rs{price}")

order_total = 0

# Take the first order
item_1 = input("Enter the name of the item you want to order: ").lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"The ordered item '{item_1}' is not available.")

# Ask if the customer wants to add another item
another_order = input("Do you want to add another item? (yes/no): ").lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to your order.")
    else:
        print(f"The ordered item '{item_2}' is not available.")

# Print the total amount
print(f"The total amount to pay is Rs{order_total}.")
