from turtle import Turtle, Screen
from random import random, seed

seed(1)


def change_color():
    R = random()
    B = random()
    G = random()

    squirtle.color((R, G, B))


squirtle = Turtle()
squirtle.speed('fastest')
squirtle.penup()
squirtle.pensize(2)
squirtle.home()
squirtle.pendown()


def draw_spirograph(size_of_gap):
    for _ in range(round(360/size_of_gap)):
        change_color()
        squirtle.circle(100)
        squirtle.right(size_of_gap)


draw_spirograph(2.235684)
squirtle.hideturtle()

# has to happen at the end
screen = Screen()
screen.exitonclick()
