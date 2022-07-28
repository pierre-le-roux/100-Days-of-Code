import string
from art import text2art

# define my alphabest
ALPHABET = list(string.ascii_lowercase)
PROGRAMS = ['encode', 'decode']
CHOICES = ['yes', 'no']

def ceasarcipher(message, number, program):
    number = number % len(ALPHABET)
    shift_message = ''

    if program == PROGRAMS[0]:
        alpha = ALPHABET
        shift_alpha = ALPHABET[number:] + ALPHABET[:number]
    else:
        alpha = ALPHABET[number:] + ALPHABET[:number]
        shift_alpha = ALPHABET

    for letter in message.lower():
        try:
            index = alpha.index(letter)
            shift_message = shift_message + shift_alpha[index]
        except:
            shift_message = shift_message + letter

    return shift_message

print(text2art('ceasar', font="rnd-large"))
print(text2art('cipher', font="rnd-large"))

running = True
while running:

    program = ''
    while program not in PROGRAMS:
        if program == '':
            program = input(f"Type '{PROGRAMS[0]}' to encrypt, type '{PROGRAMS[1]}' to decrypt:\n")

        if program not in PROGRAMS:
            program = input(f"Please specify using '{PROGRAMS[0]}' or '{PROGRAMS[1]}':\n")
    
    message = input('Type your message:\n')
    number = int(input('Type your shift number:\n'))

    print(f"Here's the {program}d message: {ceasarcipher(message, number, program)}")
    
    choice = ''
    while choice not in CHOICES:
        if choice == '':
            choice = input(f"Type '{CHOICES[0]}' if you want to run the program again. Otherwise type '{CHOICES[1]}'.\n")

        if choice not in CHOICES:
            choice = input(f"Please specify using '{CHOICES[0]}' or '{CHOICES[1]}':\n")

    if choice == CHOICES[1]:
        running = False