from string import ascii_letters, digits
from random import randrange
from icecream import ic

ic.disable()

SYMBOLS = ['!', '"', '#', '$', '%', '&', '\\', "'", '(', ')', '*', '+', ',', 
           '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^',
           '_', '`', '{' ,'|' ,'}' '~']

LETTERS = list(ascii_letters)
NUMBERS = list(digits)

print('Welcome to my Wonderful Random Password Generator!')

choice_letters = int(input('How many letters would you like in your password?\n'))
choice_numbers = int(input('How many numbers would you like in your password?\n'))
choice_symbols = int(input('How many symbols (!#$@) would you like in your password?\n'))

password = ''

for i in range(choice_letters):
    password = password + LETTERS[randrange(0, len(LETTERS))]
    ic(password)

for j in range(choice_numbers):
    random_position = randrange(0, len(password))
    password = password[:random_position] + NUMBERS[randrange(0, len(NUMBERS))] + password[random_position:]
    ic(password)

for k in range(choice_symbols):
    random_position = randrange(0, len(password))
    password = password[:random_position] + SYMBOLS[randrange(0, len(SYMBOLS))] + password[random_position:]
    ic(password)

print(f"Here is your random password: {password}")