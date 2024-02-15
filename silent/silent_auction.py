import art
import os
clear = lambda: os.system('cls')

test_dict = {"line1": "the first line",
             "line2": "the second line",
             "line45": {'line4': "the 4th line",
                        'line5': "the 5th line"}}

test_dict["line1"] = "Not the first line"

test_dict["line3"] = "Now the third line"

travel_log_dict = {'France': {'country': 'France', 'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visits': 12}, 'Germany':
{'country': 'Germany', 'cities_visited': ['Hamburg', 'Berlin', 'Stuttgart'], 'total_visits': 10} 
}

travel_log_array = [ {'country': 'France', 'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visits': 12},
{'country': 'Germany', 'cities_visited': ['Hamburg', 'Berlin', 'Stuttgart'], 'total_visits': 10} 
]
# print(travel_log[1]['country'])

new_city = {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  }

# travel_log.append(new_city)


print(travel_log_array[1]['country'])
print(travel_log_dict['France']['country'])

###############################################################################

# more_bidding = True

# print(art.logo)
# print("Welcome to the secret auction")
# bids = {}

# def calculate_winner(all_bids):
#   highest_bid = 0
#   highest_bidder = ''
#   for bidder in all_bids:
#     if all_bids[bidder] > highest_bid:
#        highest_bid = all_bids[bidder]
#        highest_bidder = bidder
  
#   print(f'The winner is {highest_bidder} with a big of ${highest_bid}')

# while more_bidding:
#     name = input('Please state your name: ')
#     amount_bid = int(input('Please state the amount to bid: '))
    
#     bids[name] = amount_bid

#     more_bid = input('Would you like to continue? \'yes\' or \'no\' ').lower()
    
#     clear()

#     if more_bid not in ['yes', 'no'] :
#         print('Read properly')

#     elif more_bid == 'no':
#       calculate_winner(bids)
#       more_bidding = False


# print(bids)
  