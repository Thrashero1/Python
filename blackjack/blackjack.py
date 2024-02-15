import random
import os
clear = lambda: os.system('cls')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print('Let\'s play BalckJack!')

keep_playing = True

def starting_hand():
    player = []
    for x in range (0,2):
        random_card = random.randint(0, len(cards)-1)
        player.append(cards.pop(random_card))
        
    if sum(player) != 21 and 11 in player:
        player.remove(11)
        player.append(1)
    return player

def deal_card(player, total):
    random_card = random.randint(0, len(cards)-1)
    player.append(cards.pop(random_card))
    print(f'Your new card is {player[-1]}')
    if sum(player) != 21 and 11 in player:
        player.remove(11)
        player.append(1)
    total += player[-1]
    return total

while keep_playing:
    play_on = True
    dealer_turn = False

    player1 = starting_hand()
    dealer = starting_hand()

    total_play1 = sum(player1)
    total_dealer = sum(dealer)

    print(f'Your starting hand is {player1} with a total of {total_play1}')
    print(f'The dealer has the card {dealer[0]} showing')

    if total_play1 > 21:
        print("Sorry you have burst, the dealer wins")
        play_on = False    
    elif total_play1 == 21:
        print("BlackJack!! You have won!!")
        play_on = False
    else:
        choice = input('Do you want to hit of stand? ').lower()
        if choice == 'stand':
            play_on = False
            dealer_turn = True




    while play_on:
        total_play1 = deal_card(player1, total_play1)
        print(total_play1)
        if total_play1 >21:
            print("Sorry you have burst, the dealer wins")
            play_on = False
            break
        choice = input('Do you want to hit of stand? ').lower()

        if choice == 'stand':
            play_on = False
            dealer_turn = True

        if total_play1 > 21:
            print("Sorry you have burst, the dealer wins")
            play_on = False
            dealer_turn = True   

    while dealer_turn:
        if total_dealer < 17:
            total_dealer = deal_card(dealer, total_dealer)
            if total_dealer > 21:
                print(f'The dealer has {dealer} with a total of {total_dealer} The dealer burst and so you win')
                break
        elif total_dealer >= 17:
            dealer_turn = False
            if total_dealer == 21:
                print(f'The dealer has {dealer} with a total of {total_dealer} BlackJack, dealer wins!')
            elif total_play1 > total_dealer:
                print(f'The dealer has {dealer} with a total of {total_dealer} well done you have won!')
            elif total_play1 == total_dealer:
                print(f'The dealer has {dealer} with a total of {total_dealer} It is a draw, dealer wins')
            else:
                print(f'The dealer has {dealer} with a total of {total_dealer} The dealer has a higher amount, dealer wins')

    
    another_game = input('Do you wanna have another game, \'Yes\' or \'No\'? ').lower()
    clear()
    if another_game =='no':
        keep_playing = False
        