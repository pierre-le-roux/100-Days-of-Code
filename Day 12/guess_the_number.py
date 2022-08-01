from cgi import test
from art import text2art
from random import randint

# Game logo
LOGO = text2art(text='Guess the Number', font='random')

DIFFICULTY = {'easy': 10,
               'medium': 7,
               'hard': 5}


def choose_difficulty():
    """asks the player to choose a difficulty and
    return the number of guesses based on the selection"""

    difficulties = list(DIFFICULTY.keys())
    choice = input(f'Please choose your difficult {difficulties}? ').lower()

    # while option
    # while choice not in difficulties:
    #     print('Invalid difficulty.')
    #     choice = input(f'Please choose your difficult {difficulties}').lower()

    # if option
    if choice not in difficulties:
        print('Invalid difficulty.')
        return choose_difficulty()
    return DIFFICULTY[choice]


def get_guess(guess_count):
    """asks the player to make a guess"""
    print(f'You have {guess_count} guesses remaining.')
    choice = ''

    while type(choice) != int:
        try:
            choice = int(input('Guess a number: '))
        except:
            print('Please choose a integer.')
    
    return choice


def calculate_position(guess, guess_count, random_number):
    """function to return if guess it too high or too low"""

    if guess > random_number:
        print('Too High.')
    elif guess < random_number:
        print('Too low')
    else:
        print(f'You got it! The answer was {random_number}')
    
    if guess_count > 1:
        print('Guess again.')
    else:
        print('You lost to a robot choosing a random number.')

    return guess_count - 1



def main(debug_mode = False):
    """function that runs the game"""

    # specifying the random number to start the game
    random_number = randint(1, 100)

    # create a debug mode to test the game and know the number
    if debug_mode:
        print(f'Pzzt, the correct number is {random_number}.')

    # print logo and introduce the game
    print(LOGO)
    print("I'm thinking of a number between 1 and 100.")

    # ask the player to choose the difficulty
    guess_count = choose_difficulty()

    guess = 0

    while guess != random_number and guess_count > 0:
        guess = get_guess(guess_count)
        guess_count = calculate_position(guess, guess_count, random_number)

        


# This means that the main function will only 
# run when guess_the_number.py is run directly
if __name__ == '__main__':
    main()