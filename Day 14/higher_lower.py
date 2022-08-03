# imports
from art import text2art
from fake_data  import data
from random import randrange


# ascii art
logo = text2art('Higher\nLower', font='random')

# future enchancement (instaloader for live data)
# import instaloader
# get random profiles
# display name and ask higher/lower follower

# choose two random points of data (not the same)
def get_data(previous_a = None, previous_b = None):
    if previous_b == None:
        random_a = randrange(len(data))
    else:
        random_a = data.index(previous_b)

    equal = True
    while equal:
        random_b = randrange(len(data))
        if random_b != random_a and random_b != previous_a:
            equal = False

    return data[random_a], data[random_b]

# display A vs B, ask Higher or Lower

# correct? add +1 score and ask B vs C (C != A)

# wrong? game over and print score

def main():
    print(logo)

if __name__ == '__main__':
    main()