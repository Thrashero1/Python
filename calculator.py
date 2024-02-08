



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

math_functions = {'+': add,
                  '-': subtract,'/': divide,'*': multiply}

continue_calc = True

number1 = int(input('Choose a number: '))

while continue_calc:     
    operation =  input('what wou;d you like to choose? + - * and /: ')
    number2 = int(input('Choose another number: '))

    answer = math_functions[operation](number1, number2)

    print(f'the current answer is {answer}')
    cont = input('would you want to continue calculating? \'y\' and \'n\': ').lower()

    if cont == 'n':
        continue_calc = False
    else:
        number1 = answer