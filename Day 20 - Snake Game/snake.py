from turtle import Turtle

STARTING_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()

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

        self.segments[-1].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[-1].setheading(90)

    def down(self):
        self.segments[-1].setheading(270)

    def left(self):
        self.segments[-1].setheading(180)

    def right(self):
        self.segments[-1].setheading(0)
