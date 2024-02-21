from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_m = CoffeeMaker()
money = MoneyMachine()

machine_on = True

selection = menu.get_items()

while machine_on:
    choice = input(f'What you like? {selection} or a \'Report\' or turn \'Off\' the machine? ').lower()
    if choice == 'report':
        coffee_m.report()
        money.report()
    elif choice == 'off':
        print('Thanks and goodbye')
        machine_on = False
    else:
        drink = menu.find_drink(choice)
        ingredients = coffee_m.is_resource_sufficient(drink)
        if ingredients:
            print(f'That will be {drink.cost} please')
            correct_payment = money.make_payment(drink.cost)
            if correct_payment:
                coffee_m.make_coffee(drink)
        