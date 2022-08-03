############DEBUGGING#####################

# Describe Problem
def my_function():
    # loops from 1 to 20 but stops before 20
    for i in range(1, 21):
        if i == 20:
            print("You got it")
my_function()

# Reproduce the Bug
from random import randint
# list goes from 0 - 5
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# random int from 1 - 6
dice_num = randint(0, 5)
# list index out of range
print(dice_imgs[dice_num])

# Play Computer
# ask birth year, but for 1994 you get no output
year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# Fix the Errors
# input doesn't get converted to int
age = int(input("How old are you?"))
if age > 18:
    # print not indented and f-string not completed
    print(f"You can drive at age {age}.")

#Print is Your Friend
# pages = 0
# word_per_page = 0
# get page and and words per page
# why declare variables beforehand?
pages = int(input("Number of pages: "))
# double == instead of = makes for a boolean check
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
    # empty b_list
    b_list = []
    for item in a_list:
        # not indented
        new_item = item * 2
        b_list.append(new_item)

    print(b_list)

mutate([1,2,3,5,8,13])