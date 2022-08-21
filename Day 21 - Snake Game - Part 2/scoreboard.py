from turtle import Turtle

FONT = ("Courier", 14, "bold")
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self, screen_width):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.score = 0
        x_location = 0
        y_location = screen_width/2 - 20
        self.goto(x_location, y_location)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}',
                   False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over',
                   False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
