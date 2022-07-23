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

choice_1 = input('Everyone is looking for transportation, what do you want to do? Wait of a boat or try to find your own transport?').lower()

if choice_1 == 'wait':
    print('Three ships arrive within the hour. One red, one green and one blue.')
    choice_2 = input('which do you choose for your journey? (red, green or blue').lower()