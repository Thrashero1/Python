import random

number_turns = 0

print('Welcome to the guessing game!')
print('I am guessing a number between 1 and 100, can you guess which it is?!')
WINNING_NUMBER =  random.randint(1, 100)
difficulty = input("would you like the hard or the easy game? ").lower()

if difficulty == 'easy':
    number_turns = 10
else:
    number_turns = 5

print(f'You have {number_turns} turns to try and guess the number!')

def check_number(player_choice):
    if player_choice > WINNING_NUMBER:
        print('Too high')
        return False
    elif player_choice < WINNING_NUMBER:
        print('Too low')
        return False
    else:
        print(f'Well done! The number was in fact {WINNING_NUMBER}')
        return True
    
def game(turns):
    guessed = False
    while not guessed and turns > 0:
        print(f'You have {turns} attempts left')
        try:
            chosen_num =  int(input('Choose a number: '))
        except:
            print('forgot to write a number')
            chosen_num =  int(input('Choose a number: '))
        turns -= 1
        guessed = check_number(chosen_num)
        if turns < 1 and guessed == False:
            print(f'sorry the number was in fact {WINNING_NUMBER}')

game(number_turns)