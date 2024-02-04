import random
import hangman_words
import hangman_art
import os
clear = lambda: os.system('cls')


print(hangman_art.logo)

stages = hangman_art.stages

words = hangman_words.word_list

blanks = []
random_word = random.choice(words)
print(f'The chosen word is {random_word}')

word_length = len(random_word)

for x in range(word_length):
    blanks.append('_')

guessed = False

number_lives = 6

print(*blanks)
while guessed == False and number_lives >= 0:
    guessed_letter = input('Choose a letter: ').lower()
    clear()
    print(f'your chosen letter is {guessed_letter}')

    if guessed_letter in blanks:
            print("already guessed that letter, try again")
            letter_in_word = True
            
    for y in range(word_length):      
        if(guessed_letter == random_word[y]):
            blanks[y] = guessed_letter
            letter_in_word = True

    if guessed_letter not in random_word:
        print(' lost a live')
        print(stages[number_lives])
        number_lives -= 1

    print(*blanks)

    if '_' not in blanks:
        guessed = True
        print('You have won')

if number_lives < 0:
    print(f"Oh no!! You lost!!.... The word was {random_word}")



