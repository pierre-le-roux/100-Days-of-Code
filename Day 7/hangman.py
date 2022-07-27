from random_word import RandomWords
from art import text2art
from os import system

HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# create random word object
r = RandomWords()

# generate my random word from Noun or Verb, min of 5 characters
got_word = False
while not got_word:
    word = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minLength=5, maxLength=8)

    if word != None:
        got_word = True

print(word)

# generate my word display
display = ['_']*len(str(word))
# print(''.join(display))

# print welcoming screen
print(text2art('Hangman', font="big"))

# define life points (no of guesses)
used_letters = []
life_points = 6
still_alive = True
while still_alive:
    # Get a letter input from user
    letter = input('Guess a letter: ')
    # block player from putting in multiple letters
    while len(letter) > 1:
        letter = input('Please guess only a single letter: ')

    if letter in used_letters:
        print(f'You\'ve already used {letter}, please guess another letter.')
    else:
        system('cls')
        
        # if a letter is guess, it's added to the used list
        used_letters.append(letter)
        
        # find the possible positions the letter is in the word
        positions = [pos for pos, char in enumerate(word) if char == letter]

        # if positions are populated
        if len(positions) > 0:
            for pos in positions:
                display[pos] = letter
            print(''.join(display))
        else:
            if life_points == 1:
                still_alive = False
                life_points -= 1
                print(''.join(display))
                print('You lost your last life, Game Over')
            else:
                life_points -= 1
                print(''.join(display))
                print(f'You guessed {letter}, that\'s not in the word. You lose a life. {life_points} guesses remaining')
        
        print(used_letters)
        print(HANGMAN[-life_points-1])

    if '_' not in display:
        print(f'You\'ve won the game with {life_points} guess(es) remaining.')
        still_alive = False