import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


total_chars = int(input('How many chars in the password? \n'))
total_nums = int(input('How many of those chars are to be numbers in the password? \n'))
total_symbols = int(input('How many of those chars are to be symbols in the password? \n'))

random_position = -1

if total_chars < total_nums + total_symbols:
    print('learn to add up son!')
else:
    letter_length = len(letters)
    numbers_length = len(numbers)
    symbols_length = len(symbols)
    password = ''

    list_pass = []

    for x in range(total_chars):
        random_letter = int(random.random() * letter_length)
        list_pass.append(letters[random_letter])

    for y in range(total_nums): 
        random_num = int(random.random() * numbers_length)
        list_pass.append(numbers[random_num])


    for z in range(total_symbols): 
        random_symbole = int(random.random() * symbols_length)
        list_pass.append(symbols[random_symbole])
    
    random.shuffle(list_pass)

    for passw in range(len(list_pass)):
        password += list_pass[passw]

    print(password)

