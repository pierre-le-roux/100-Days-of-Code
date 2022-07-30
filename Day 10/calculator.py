from ascii_art import CALCULATOR
from art import text2art
from functions import *


OPERATORS = {'+':plus, 
            '-':minus, 
            '*':product, 
            '/':devide}

def calculator():
    calculate_more = True
    num_1 = float(input('What\'s your first number? '))
    
    while calculate_more:
        operator = input(f'Choose operation {list(OPERATORS.keys())}? ')
        num_2 = float(input('What\'s your second number? '))
        answer = OPERATORS[operator](num_1, num_2)

        print(f"{num_1} {operator} {num_2} = {answer}")
        
        choice = input(f"Type 'y' to calculate using {answer}, or 'n' to start a new calculation. ")
        if choice == 'y':
            num_1 = answer
        else:
            num_1 = float(input('What\'s your first number? '))


def main():
    print(CALCULATOR)

    calculator()

if __name__ == '__main__':
    main()