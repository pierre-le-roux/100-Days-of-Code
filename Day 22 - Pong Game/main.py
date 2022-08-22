# from time import sleep
from time import sleep
from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
from settings import WIDTH, HEIGHT

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.tracer(0)

scoreboard = Scoreboard()
player_1 = Player(1)
player_2 = Player(2)
ball = Ball()

screen.listen()
screen.onkey(key='w', fun=player_1.up)
screen.onkey(key='s', fun=player_1.down)
screen.onkey(key='Up', fun=player_2.up)
screen.onkey(key='Down', fun=player_2.down)


def main():
    gaming = True
    while gaming:
        sleep(0.05)
        screen.update()
        ball.check_boarders()
        ball.move()

        # ball hit by player
        # ic(ball.distance(player_1))
        ball.update_angle(player_1)
        ball.update_angle(player_2)

        # ball collide with goal area behind player
        if abs(ball.xcor()) > WIDTH/2:
            scoreboard.update_score(ball.xcor() > 0)
            player_1.refresh()
            player_2.refresh()
            ball.refresh()
            main()

    screen.exitonclick()


if __name__ == '__main__':
    main()
