import random
from data import data
import os
clear = lambda: os.system('cls')

celebreties = data
not_lost = True


def select_celeb(choice_letter):
    random_celeb = random.randint(0, len(celebreties))
    celeb = celebreties.pop(random_celeb)
    print(f'Compare {choice_letter}: {celeb['name']} a {celeb['description']} from {celeb['country']} with {celeb['followers']}')
    return celeb


def game(celeb1, celeb2, score):
    choice = input('Choose which of the 2 has more followers? \'A\' or \'B\'').lower()
    if choice == 'a':
        if celeb1['followers'] > celeb2['followers']:
            clear()
            score += 1
            print(f'well done you are correct, your current score is {score}')
            print(f'Compare \'A\': {celeb1['name']} a {celeb1['description']} from {celeb1['country']} with {celeb1['followers']}')
            celeb_2 = select_celeb('B')
            game(celeb1, celeb_2, score)
        else:
            clear()
            print(f'Oh no you are wrong, your final score is {score}')
    else:
        if celeb1['followers'] < celeb2['followers']:
            clear()
            score += 1
            print(f'well done you are correct, your current score is {score}')
            celeb_1 = select_celeb('A')
            print(f'Compare \'B\': {celeb2['name']} a {celeb2['description']} from {celeb2['country']} with {celeb2['followers']}')
            game(celeb_1, celeb2, score)
        else:
            clear()
            print(f'Oh no you are wrong, your final score is {score}')


print('Welcome to the Higher or Lower game. Try to guess which of the 2 celebrities has the more followers each round')

celeb_1 = select_celeb('A')

celeb_2 = select_celeb('B')

game(celeb_1, celeb_2, 0)
    