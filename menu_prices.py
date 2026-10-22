menu = {
    "Burger": 12,
    "Pizza": 15,
    "Fries": 5
}

for item in menu:
    print(item + ": $" + str(menu[item]))

user_input = input("What would you like to order? ")

if user_input in menu:
    print(user_input + ": $" + str(menu[user_input]))
else:
    print("That item is not on the menu.")

