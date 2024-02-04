import random

# print('Welcome to the Band Name Generator')
# city = input('What is the name of the city you were born in?\n')
# pet = input('What is the name of your first pet?\n')
# print('your band name is: ' + city + ' ' + pet + '\n \n')

###############################################################################

# print('Welcome to the tip calculator')
# bill = float(input('What was the total of you bill?   '))

# tip_percentage = float('1.' + input('what percentage tip would you like to give? 10, 12 or 15   '))

# split = int(input('How many people to split the bill   '))

# amount_per_person = (bill * tip_percentage) / split

# final_am = '{:.2f}'.format(amount_per_person)

# print(f'The final amount {split} people need to pay is {final_am}')

##############################################################################

# test = int(input('write any number from 1 to 100:   '))

# if test < 50:
#     print('oh that is close but not close enough')
#     print('wanna try again?')
# elif test >=50 and test <= 100:
#     print('that is the right amount')
# else: 
#     print('Whoah that is too high mate!')
# tested = 'David'

###############################################################################

# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# names = name1 + name2
# namesLower = names.lower()

# t = namesLower.count('t')
# r = namesLower.count('r')
# u = namesLower.count('u')
# e = namesLower.count('e')
# trueCount = str(t + r + u + e)

# l = namesLower.count('l')
# o = namesLower.count('o')
# v = namesLower.count('v')
# e = namesLower.count('e')
# loveCount = str(l + o + v + e)
# finalNum = int(trueCount + loveCount)

# if finalNum <10 or finalNum >90:
#   print(f'Your score is {finalNum}, you go together like coke and mentos.')
# elif finalNum >40 and finalNum <50:
#   print(f'Your score is {finalNum}, you are alright together.')
# else:
#   print(f'Your score is {finalNum}.')

################################################################################
names = ['Dave', 'Arlinda', 'John', 'Claire', 'Mike', 'Rach']
count =  0
for name in names:
    randomN = int(random.random() * 6)
    print(names[randomN])    
    count += 1
    print(count)

whatTTT = []
whatTTT = input().split
print(f'these are the nums: {type(whatTTT)}')

# # Creating a Multi-Dimensional List
# # (By Nesting a list inside a List)
# List = [['Geeks', 'For'], ['Geeks']]
 
# # accessing an element from the
# # Multi-Dimensional List using
# # index number
# print("Accessing a element from a Multi-Dimensional list")

# List[0][1] = 'Test'
# print(List[0][1])
# print(List[1][0])