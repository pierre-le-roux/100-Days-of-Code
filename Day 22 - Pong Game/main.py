# from time import sleep
from turtle import Screen
from player import Player
from settings import WIDTH, HEIGHT

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')

player_1 = Player(1)
player_2 = Player(2)

screen.listen()
screen.onkey(key='w', fun=player_1.up)
screen.onkey(key='s', fun=player_1.down)
screen.onkey(key='Up', fun=player_2.up)
screen.onkey(key='Down', fun=player_2.down)


def main():

    # gaming = True
    # while gaming:
    #     sleep(0.1)

    screen.exitonclick()


if __name__ == '__main__':
    main()
