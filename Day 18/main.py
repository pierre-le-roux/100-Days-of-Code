from turtle import Turtle, Screen
from random import random


def change_color():
    R = random()
    B = random()
    G = random()

    squirtle.color(R, G, B)


squirtle = Turtle()
squirtle.speed('fastest')
squirtle.penup()
squirtle.goto(-38, 400)
squirtle.pendown()
squirtle.shape('turtle')
squirtle.color('black', 'orange')

for i in range(1, 40):
    angle = 360/(i+2)
    change_color()
    for j in range(i+2):
        squirtle.fd(75)
        squirtle.right(angle)

# has to happen at the end
screen = Screen()
screen.exitonclick()
