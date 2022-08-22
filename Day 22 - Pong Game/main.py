# from time import sleep
from time import sleep
from turtle import Screen
from player import Player
from ball import Ball
from settings import WIDTH, HEIGHT

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.tracer(0)

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
        sleep(0.1)
        screen.update()
        ball.check_boarders()
        ball.move()

        # ball hit by player
        ball.update_angle(player_1.xcor(), player_1.ycor())
        ball.update_angle(player_2.xcor(), player_2.ycor())

        # ball collide with goal area behind player
        if abs(ball.xcor()) > WIDTH/2:
            ball.refresh()
            main()

    screen.exitonclick()


if __name__ == '__main__':
    main()
