from turtle import Turtle, Screen
from prettytable import PrettyTable

skillie = Turtle()
print(skillie)
skillie.shape('turtle')
skillie.color('black', 'dark turquoise')
skillie.forward(300)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

table = PrettyTable()
table.add_column('Pokemon', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'
print(table.align)
print(table)
