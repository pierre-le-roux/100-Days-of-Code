# imports
from secrets import choice
from art import text2art
from fake_data  import data
from random import randrange
from os import system


# ascii art
logo = text2art('Higher\nLower', font='random')

# future enchancement (instaloader for live data)
# import instaloader
# get random profiles
# display name and ask higher/lower follower

# clean output screen
def clear():
    system('cls')

# choose two random points of data (not the same)
def get_data(history):
    if history:
        random_a = data.index(history[1])
        previous_b = data.index(history[0])
    else:
        random_a = randrange(len(data))
        previous_b = 0

    equal = True
    while equal:
        random_b = randrange(len(data))
        if random_b != random_a and random_b != previous_b:
            equal = False

    return [data[random_a], data[random_b]]

# display A vs B, ask Higher or Lower
def display_choices_get_input(choices):
    a = choices[0]
    b = choices[1]
    print(f"{a['name']}, is a {a['description']} from {a['country']}")
    print(text2art('vs', font='random'))
    print(f"{b['name']}, is a {b['description']} from {b['country']}")

    return input("Who has the most followers, 'A', or 'B'? ").lower()

# correct? add +1 score and ask B vs C (C != A)8
def check_answer(choices, input):
    if input == 'a':
        if choices[0]['follower_count'] > choices[1]['follower_count']:
            return True
        else:
            return False
    else:
        if choices[0]['follower_count'] < choices[1]['follower_count']:
            return True
        else:
            return False

# wrong? game over and print score
def game_over(correct, score):
    if correct:
        score += 1
        clear()
        print(f'You are correct, current score: {score}')
    else:
        clear()
        print(f'You are wrong, your score is: {score}')

    return score


def main():
    print(logo)

    correct = True
    choices = []
    score = 0
    while correct:
        choices = get_data(choices)

        user_input = display_choices_get_input(choices)

        correct = check_answer(choices, user_input)

        score = game_over(correct, score)

    if input("Would you like to play again, 'y' or 'n'? ").lower() == 'y':
        clear()
        main()


if __name__ == '__main__':
    main()