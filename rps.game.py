import random

rock = '''
Rock \n
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper \n
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors \n
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

player_choice = int(input('0 for Rock, 1 for paper, 2 for scissors: '))

if player_choice > 2 or player_choice < 0:
    print('learn how to read... you lose!!')
else:
    computer_choice = random.randint(0,2)

    print(f'You chose \n{images[player_choice]}')

    print(f'The computer chose \n{images[computer_choice]}')

    if computer_choice == player_choice:
        print('This is a draw')
    elif computer_choice == 0 and player_choice == 2 or computer_choice == 1 and player_choice == 0 or computer_choice == 2 and player_choice == 1:
        print('The computer wins')
    else:
        print('You have won') 