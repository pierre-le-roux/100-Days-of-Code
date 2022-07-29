# silent auction
# who are you?
# How much would you like to bid? R
# Are there any other bidders?
# Show the bidder name with the highest bid

from ascii_art import GAVEL
from os import system

def clear():
    system('cls')

def bid():
    name = input('What is your name? ')
    bid_amount = input('How much would you like to bid? R')
    
    return name, bid_amount

def max_bid(bids):
    return max(bids, key=bids.get)

def silent_auction():
    new_bidder = True
    bids = {}

    while new_bidder:
        name, bid_ammount = bid()
        bids[name] = bid_ammount

        choice = input('Are there any other bidders (yes, no)? ')
        if choice == 'no':
            new_bidder = False
        
        clear()

    name_max_bid = max_bid(bids)
    value_max_bid = bids[name_max_bid]
    print(f'The highest bid was by {name_max_bid} with R{value_max_bid}. Congratulations!')

def main():
    print(GAVEL)
    print('Welcome to the silent auction.')

    silent_auction()

if __name__ == "__main__":
    main()