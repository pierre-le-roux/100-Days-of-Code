from logging import exception
from random import randrange

# rock (0), paper (1), scissors (2)
drawings = [
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

game_end = False
score = [0, 0]

while game_end == False:

    made_choice = False

    while made_choice == False:
        try:
            player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
            if 0 <= player_choice <= 2:
                made_choice = True
            else:
                print('please specify an integer of either 0, 1 or 2')
        except:
            print('please specify an integer of either 0, 1 or 2')
        
        

        ai_choice = randrange(0, 3)

    print(drawings[player_choice])
    print('AI chose:')
    print(drawings[ai_choice])

    if player_choice == ai_choice:
        print('Draw')
    elif player_choice == 0:
        if ai_choice == 1:
            print('You Lose')
            score = [score[0], score[1]+1]
        elif ai_choice == 2:
            print('You Win')
            score = [score[0]+1, score[1]]
    elif player_choice == 1:
        if ai_choice == 0:
            print('You Win')
            score = [score[0]+1, score[1]]
        elif ai_choice == 2:
            print('You Lose')
            score = [score[0], score[1]+1]
    elif player_choice == 2:
        if ai_choice == 0:
            print('You Lose')
            score = [score[0], score[1]+1]
        elif ai_choice == 1:
            print('You Win')
            score = [score[0]+1, score[1]]

    print(f'Current score: You {score[0]}, AI {score[1]}')
    play_again_choice = False

    while play_again_choice == False:
        play_again = input('Would you like to play again [yes, no]?\n').lower()

        if play_again == 'yes':
            play_again_choice = True
        elif play_again == 'no':
            print(f'Final score: You {score[0]}, AI {score[1]}')
            game_end = True
            play_again_choice = True
        else:
            print('Please type a valid answer.')
