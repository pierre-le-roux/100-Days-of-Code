from random import choice
from turtle import Turtle
from settings import HEIGHT

SPEED = [-15, 15]
SIZE = 30


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.home()
        self.penup()
        self.shape('square')
        self.color('white')
        self.turtlesize(1.5, 1.5, 1)
        self.start_angle()
        self.showturtle()

    def start_angle(self):
        self.x_speed = choice(SPEED)
        self.y_speed = choice(SPEED)

    def check_boarders(self):
        if abs(self.ycor()) + SIZE > HEIGHT/2:
            self.y_speed = self.y_speed * -1

    def update_angle(self, player_x, player_y):
        if abs(player_x - self.xcor()) <= SIZE + abs(self.x_speed):
            self.x_speed = self.x_speed * -1

            if player_y > self.ycor():
                self.y_speed = SPEED[0]
            else:
                self.y_speed = SPEED[1]

    def move(self):
        self.goto(self.xcor() + self.x_speed,
                  self.ycor() + self.y_speed)

    def refresh(self):
        self.clear()
        self.hideturtle()
        self.home()
        self.start_angle()
        self.showturtle()