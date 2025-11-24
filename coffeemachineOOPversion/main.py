from coffeemachineOOPversion.coffee_maker import CoffeeMaker
from coffeemachineOOPversion.menu import Menu,MenuItem
import coffee_maker
from coffeemachineOOPversion.money_machine import MoneyMachine

# create your object classes
money_mechine = MoneyMachine()
menu = Menu()
coffee = CoffeeMaker()
#ask the user what he wants


turn_on = True

while turn_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        turn_on = False
    elif choice == "report":
        coffee.report()
        money_mechine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            money_mechine.make_payment(drink.cost)
            coffee.make_coffee(drink)

        else:
            coffee.is_resource_sufficient(drink)
