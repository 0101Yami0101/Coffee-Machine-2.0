from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine() #Obj 
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    privatekey = 10101
    
    choice = input(f"What would you like: {menu.get_items()}")
    if choice == "off":
        masterKey = int(input("Enter Master Key"))
        if masterKey == privatekey:
            is_on = False
    elif choice == "report":
        masterKey = int(input("Enter Master Key"))
        if masterKey == privatekey:
            coffee_maker.report()
            money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


