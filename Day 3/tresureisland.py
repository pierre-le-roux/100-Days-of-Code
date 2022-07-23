print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# choice 1 - Wait for boat? (correct) | Search for transport (board leaves without you)
# choice 2 - 3 boat choices (red, green or blue), red - sinks (attack by kraken), green - trap (stranded on desert island), blue - takes you to destination
# choice 3 - cave, location on map, stay on ship - dead (creature), tresure (correct), lazy bones

print('Welcome adventurer to the port town of Arcland.')
print('Your mission is to find the treasure located on this map.')
print('Good luck and may the best adventurer win!')

choice_1 = input('Everyone is looking for transportation, what do you want to do? WAIT of a boat or try to FIND your own transport? ').lower()

if choice_1 == 'wait':
    print('Three ships arrive within the hour. One RED, one GREEN and one BLUE.')
    choice_2 = input('which do you choose for your journey? ').lower()

    if choice_2 == 'red':
        print('Your adventure is off to a good start only to end misreably when the kraken attacks your boat and everyone dies.\nGame Over')
    elif choice_2 == 'green':
        print('You chose the boat with the slimiest looking crew. Good luck, because it\'s a trap. You\'ve been captured and thrown overboard after they strip you of your pocessions. Game Over')
    elif choice_2 == 'blue':
        print('The majestic blue sails set sail to Treasure Island. Soon the treasure will be yours.')
        print('You arive on Treasure Island and begin searching for clues.')
        print('You\'ve found 3 locations where the treasure may be hidden, a cave to the NORTH, the WEST beach or an Oasis to the SOUTH.')
        choice_3 = input('Which location would you like search at? ').lower()
        
        if choice_3 == 'north':
            print('You mistep in the dark cave, fall, hit your head and die. Game Over')
        elif choice_3 == 'west':
            print('Today must be your lucky day. You\'ve found the treasure. You Win')
        elif choice_3 == 'south':
            print('You get distracted by the beautiful blue water and start swimming in the oasis. You tire and drown. Game Over')

elif choice_1 == 'find':
    print('You wander around aimlessly and before you could find transportation all the boats leave. Game Over')
