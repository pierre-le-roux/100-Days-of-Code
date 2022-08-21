from turtle import Turtle
from random import choice
# from icecream import ic

STAMP_SIZE = 20


class Food(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color('blue')
        self.speed('fastest')
        width = int(screen_width / 2)-20
        height = int(screen_height / 2)-20
        self.x_locations = range(-width, width, 20)
        self.y_locations = range(-height, height, 20)
        self.refresh()

    def refresh(self):
        random_x = choice(self.x_locations)
        random_y = choice(self.y_locations)
        self.goto(random_x, random_y)
