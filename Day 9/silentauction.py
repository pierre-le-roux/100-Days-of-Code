# silent auction
# who are you?
# How much would you like to bid? R
# Are there any other bidders?
# Show the bidder name with the highest bid

gavel = """
     ___________
     \         /
      )_______(
      |"""""""|_.-._,.---------.,_.-._
      |       | | |               | | ''-.
      |       |_| |_             _| |_..-'
      |_______| '-' `'---------'` '-'
      )"""""""(
     /_________\
     `'-------'`
   .-------------.
  /_______________\
"""

def bid():
    name = input('What is your name? ')
    bid_amount = input('How much would you like to bid? R')
    
    return name, bid_amount

def max_bid(bids):
    return max(bids, key=bids.get)