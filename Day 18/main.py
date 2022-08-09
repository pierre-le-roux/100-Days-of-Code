from turtle import Turtle, Screen
from random import randint, random, randrange, choice


def change_color():
    R = random()
    B = random()
    G = random()

    squirtle.color(R, G, B)


squirtle = Turtle()
squirtle.speed('fastest')
squirtle.penup()
# squirtle.goto(-38, 400)
squirtle.pensize(15)
squirtle.home()
squirtle.pendown()
squirtle.shape('turtle')
squirtle.color('black', 'orange')

for _ in range(50000):
    change_color()
    squirtle.fd(25)
    squirtle.setheading(choice([0, 90, 180, 270]))

squirtle.hideturtle()

# has to happen at the end
screen = Screen()
screen.exitonclick()
