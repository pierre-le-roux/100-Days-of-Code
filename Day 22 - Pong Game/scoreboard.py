from turtle import Turtle
from settings import HEIGHT

FONT = ("Courier", 36, "bold")
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.pencolor('white')
        self.player_1 = 0
        self.player_2 = 0
        self.draw_scoreboard()

    def draw_center(self):
        self.penup()
        self.goto(0, -(HEIGHT/2))
        self.pensize(10)
        for num in range(round(HEIGHT/20)):
            if num % 2 == 0:
                self.pendown()
                self.goto(0, self.ycor()+50)
            else:
                self.penup()
                self.goto(0, self.ycor()+50)
        self.penup()

    def draw_scoreboard(self):
        self.clear()
        self.draw_center()
        self.goto(0, (HEIGHT/2) - 60)
        self.write(f'{self.player_1}\t{self.player_2}',
                   False, align=ALIGNMENT, font=FONT)

    def update_score(self, player_1_score):
        if player_1_score:
            self.player_1 += 1
        else:
            self.player_2 += 1

        self.draw_scoreboard()
