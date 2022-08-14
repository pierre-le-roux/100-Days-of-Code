from turtle import Turtle, Screen, colormode

colormode(255)

leonardo = Turtle()
michelangelo = Turtle()
donatello = Turtle()
raphael = Turtle()
skillie = Turtle()

screen = Screen()
screen.setup(width=500, height=400)

guess = screen.textinput(title='Guess',
                         prompt='Who will win the race? Enter a colour:')

print(guess)

leonardo.color((0, 170, 230))
michelangelo.color((255, 165, 0))
donatello.color((170, 27, 221))
raphael.color((227, 51, 28))
skillie.color((76, 156, 35))

leonardo.penup()
michelangelo.penup()
donatello.penup()
raphael.penup()
skillie.penup()

leonardo.goto(-225, 100)
michelangelo.goto(-225, 50)
donatello.goto(-225, 0)
raphael.goto(-225, -50)
skillie.goto(-225, -100)

screen.exitonclick()
