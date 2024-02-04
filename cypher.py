alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(cypher_type, text, shift_amount):
    list_length = len(alphabet)
    new_text = ''
    for letter in text:
        if letter in alphabet:
            ind = alphabet.index(letter)
            if cypher_type == 'encode':
                new_index = ind + shift_amount
                if new_index >= list_length:
                    new_index = new_index - (list_length)
            else:    
                new_index = ind - shift_amount
                if new_index < 0:
                    new_index = new_index + (list_length)
            new_letter = alphabet[new_index]
            new_text += new_letter
        else:
            new_text += letter
    print(new_text)
        
still_encrypting = True
while still_encrypting:
    type_cypher = input('Would you like to endcode or decode? ')

    secret_word = input(f'Type the word to {type_cypher} ')
    shift = int(input('By how much should it be shifted? '))

    encrypt(type_cypher, secret_word, shift)
    goon = input("would you like to continue? yes or no? ")
    if goon == 'no':
        still_encrypting = False