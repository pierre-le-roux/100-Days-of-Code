from turtle import Turtle

STARTING_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[-1]

    def create_snake(self):
        for (x, y) in STARTING_POSITIONS:
            segment = Turtle('square')
            segment.penup()
            segment.color('white')
            segment.goto(x, y)
            self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments)-1):
            self.segments[i].goto(self.segments[i+1].position())

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
