MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO It needs to ask the our what kind of coffee they would like(Espresso, Latte, or Cappucino.
# TODO Once they make a choice, it tells them their total and asks for the payment.
# TODO After they pay, it gives them their coffee and change
# TODO  It then deducts the resources used from the remaining resources.
# TODO if the machine does not have enough resources, it tell the user which resource it is short on.
# TODO The machine has two hidden features of "off" and "report"

def machine_input(choice):
    """Determines what the coffee machine does based on the user's input"""
    if choice == "off":#ends the program
        print("\nTurning off Coffee Machine.")
        return 1
    elif choice == "report": #prints outs the current resources inside the coffee machine
        for key in resources:
            print(f"{key}: {coffee_machine_resources[key]}")
        print(f"Money: ${profit:.2f}")
        return 2
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino": #runs if the users choose a drink as an option
        return 3
    else: #makes the user renter a valid option
        print("\nInvalid option. Please try again")
        return 4

def check_resources(menu, original_machine_resources):
    """Compares the coffee machines current resources to the need resources to make the drink of the user's choice"""
    sample_resource = {}
    sample_resource.update(original_machine_resources)
    for key in menu[user_choice]["ingredients"]:
        if sample_resource[key] >= menu[user_choice]["ingredients"][key]:
            sample_resource[key] -= menu[user_choice]["ingredients"][key]
        else: #if the machine is short on a resource, the machine will not deliver the chosen drink
            print(f"Sorry there is not enough {key}:")
            return original_machine_resources, 0
    cost = get_payment()
    if cost == 0:
        return original_machine_resources, cost
    return sample_resource, cost

def get_payment():
    """Has the user enter coin values and calculates if they put in enough money to pay for the coffee"""
    cost = MENU[user_choice]["cost"]
    print(f"\nYour total is ${cost:.2f}")
    print("Please insert coins.")
    try:
        quarters = float(input("How many quarters? "))
        dimes = float(input("How many dimes? "))
        nickels = float(input("How many nickels? "))
        pennies = float(input("How many pennies? "))
    except ValueError:
        print("\nInvalid coin. Order refunded")
        return 0

    total_inserted_money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    if total_inserted_money >= cost:
        customers_change = total_inserted_money - cost
        print(f"\nThank you. Here is your change: ${customers_change:.2f}")
        return cost
    else:
        print("\nYou did not insert enough money. Order Refunded.")
        return 0



turned_on = True
coffee_machine_resources = resources
profit = 0.0

while turned_on:
    user_choice = input("What would you like to order? espresso/latte/cappuccino: ").lower()
    machine_output = machine_input(user_choice) #turns the machine off if the user typed in "off"
    if machine_output == 1:
        turned_on = False
    elif machine_output == 3:
        coffee_machine_resources, money_from_order = check_resources(MENU, coffee_machine_resources)
        if money_from_order != 0:
            profit += money_from_order
            print(f"Here is your {user_choice}. Enjoy!")