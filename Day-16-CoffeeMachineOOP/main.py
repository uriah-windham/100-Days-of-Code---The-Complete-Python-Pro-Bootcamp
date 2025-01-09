from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_menu = Menu()
my_money = MoneyMachine()

turned_on = True

while turned_on:
    choice = input(f"What would you like to order? {my_menu.get_items()} ").lower()
    if choice == "off": #ends the program
        print(f"\nPowering Down.")
        turned_on = False
    elif choice == "report": #prints out a list of the coffee machine's resources of profits
        my_coffee_maker.report()
        my_money.report()
    else:
        ordered_drink = my_menu.find_drink(choice) #checks if the user ordered a valid drink and returns 'None' if their order in invalid
        if ordered_drink is not None:
            if my_coffee_maker.is_resource_sufficient(ordered_drink): #checks if the coffee machine has enough resources to make the drink

                if my_money.make_payment(ordered_drink.cost): #has the user insert their coins and ensures the
                                                              #user puts in enough money for the drinks cost
                                                              #if the user pay and excess amount of money, then it gives the user their change
                                                              #adds the ordered drink's cost to the coffee machine's profits

                    my_coffee_maker.make_coffee(ordered_drink) #deducts the resources needed to make the ordered
                                                               #drink from the coffee machine's resources
                                                               #then delivered the ordered drink to user
