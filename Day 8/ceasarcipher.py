import string
from art import text2art

# define my alphabest
alphabet = list(string.ascii_lowercase)

def encode(message, number):
    number = number % len(alphabet)
    encoded_alphabet = alphabet[number:] + alphabet[:number]
    encoded_message = ''

    for letter in message.lower():
        try:
            index = alphabet.index(letter)
            encoded_message = encoded_message + encoded_alphabet[index]
        except:
            encoded_message = encoded_message + letter

    return encoded_message

def decode(message, number):
    number = number % len(alphabet)
    decoded_alphabet = alphabet[number:] + alphabet[:number]
    decoded_message = ''

    for letter in message.lower():
        try:
            index = decoded_alphabet.index(letter)
            decoded_message = decoded_message + alphabet[index]
        except:
            decoded_message = decoded_message + letter

    return decoded_message

print(text2art('ceasar', font="rnd-large"))
print(text2art('cipher', font="rnd-large"))

running = True
while running:

    program = ''
    options = ['encode', 'decode']
    while program not in options:
        program = input(f"Type '{options[0]}' to encrypt, type '{options[1]}' to decrypt:\n")

        if program not in options:
            print(f"Please specify using '{options[0]}' or '{options[1]}'.")
    
    message = input('Type your message:\n')
    number = int(input('Type your shift number:\n'))

    if program == options[0]:
        print(f"Here's the encoded message: {encode(message, number)}")
    else:
        print(f"Here's the decoded message: {decode(message, number)}")
    
    choice = ''
    options = ['yes', 'no']
    while choice not in options:
        choice = input(f"Type '{options[0]}' if you want to run the program again. Otherwise type '{options[1]}'.\n")

        if choice not in options:
            print(f"Please specify using '{options[0]}' or '{options[1]}'.")

    if choice == options[1]:
        running = False