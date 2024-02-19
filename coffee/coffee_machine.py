from menu import MENU

machine_on = True
ingredients = {
    'water': 300, 
    'milk': 200, 
    'coffee': 100}


def refil():
    ingredients['water'] = 200
    ingredients['milk'] = 200
    ingredients['coffee'] = 100 

def report():
    print (f'Water: {ingredients['water']}ml \nMilk: {ingredients['water']}ml \nCoffee: {ingredients['coffee']}g')

def get_paid():
    quaters = float(input('How many quaters?')) * 0.25
    dimes = float(input('How many dimes?')) * 0.10
    nickles = float(input('How many nickles?')) * 0.05
    pennies = float(input('How many pennies?')) * 0.01
        
    total = quaters + dimes + nickles + pennies
    return total

def ingredients_adjust(choice):
    take_money = True
    drink_ingredients = MENU[choice]['ingredients']
    for items in drink_ingredients:
        if drink_ingredients[items] > ingredients[items]:
            print(f'sorry we are low on {items} 😒')
            take_money = False
            return take_money
        ingredients[items] = ingredients[items] - drink_ingredients[items]
        return take_money
    
def check_amount(total, choice):
    if total >= MENU[choice]['cost']:
        change = total - MENU[choice]['cost']
        change = "{:.2f}".format(change)
        print(f'Here is ${change} in change \nHere is your {choice} 🍵, enjoy!')
    else:
        print('This is not enough, more money please!')
        new_total = total + get_paid()
        check_amount (new_total, choice)
    
def take_order(choice):
    if choice == 'report':
        report()
    else:
        take_money = ingredients_adjust(choice)
        if take_money:
            money_given = get_paid()
            check_amount(money_given, choice)
        
        
while machine_on:
    chosen_one =input ('What Coffee would you like? \'Espresso\', \'Cappuccino\' \'Latte\' get a \'Report\' or turn \'Off\' the machine: ').lower()
    
    if chosen_one == 'off':
        machine_on == False
    else: 
        take_order(chosen_one)
    

