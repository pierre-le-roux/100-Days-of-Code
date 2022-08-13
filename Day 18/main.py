from turtle import Turtle, Screen
from random import random, choice


def change_color():
    R = random()
    B = random()
    G = random()

    squirtle.color((R, G, B))


squirtle = Turtle()
squirtle.speed('fastest')
squirtle.penup()
squirtle.pensize(15)
squirtle.home()
squirtle.pendown()


for _ in range(50):
    change_color()
    squirtle.fd(25)
    squirtle.setheading(choice([0, 90, 180, 270]))

squirtle.hideturtle()

# has to happen at the end
screen = Screen()
screen.exitonclick()
