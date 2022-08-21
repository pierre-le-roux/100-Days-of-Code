from turtle import Turtle
from settings import WIDTH, HEIGHT

UP = 270
DOWN = 90
SIZE = 60
SPEED = 60


class Player(Turtle):

    def __init__(self, player=1):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.shape('square')
        self.speed('fastest')
        self.turtlesize(6, 1.5, 1)
        self.player = player
        self.starting_position()
        self.showturtle()

    def starting_position(self):
        if self.player == 1:
            self.goto(-(WIDTH/2 - 30), 0)
        else:
            self.goto((WIDTH/2 - 30), 0)

    def up(self):
        if self.ycor() + SIZE < HEIGHT/2:
            self.setpos(self.xcor(), self.ycor()+SPEED)

    def down(self):
        if self.ycor() - SIZE > -(HEIGHT/2):
            self.setpos(self.xcor(), self.ycor()-SPEED)
