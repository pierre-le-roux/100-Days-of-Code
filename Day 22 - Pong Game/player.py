from turtle import Turtle
from settings import WIDTH, HEIGHT

UP = 270
DOWN = 90
SIZE = 60
SPEED = 60


class Player(Turtle):

    def __init__(self, player):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.shape('square')
        self.speed('fastest')
        self.shapesize(6, 1.5, 1)
        self.player = player
        self.score = 0
        self.starting_position()
        self.showturtle()

    def starting_position(self):
        if self.player == 1:
            self.goto(-(WIDTH/2 - 32), 0)
        else:
            self.goto((WIDTH/2 - 32), 0)

    def refresh(self):
        self.hideturtle()
        self.sety(0)
        self.showturtle()

    def up(self):
        if self.ycor() + SIZE < HEIGHT/2:
            self.setpos(self.xcor(), self.ycor()+SPEED)

    def down(self):
        if self.ycor() - SIZE > -(HEIGHT/2):
            self.setpos(self.xcor(), self.ycor()-SPEED)

    def update_score(self):
        self.score += 1
