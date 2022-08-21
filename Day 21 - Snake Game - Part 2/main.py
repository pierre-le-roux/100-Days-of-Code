from turtle import Screen
from snake import Snake
from food import Food
from time import sleep
from scoreboard import Scoreboard
from icecream import ic

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food(WIDTH, HEIGHT)
scoreboard = Scoreboard(WIDTH)

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

gaming = True
while gaming:
    screen.update()
    sleep(0.1)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 5:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # Detect collision with walls.
    if (abs(snake.head.xcor()) > (WIDTH/2 - 1) or
            abs(snake.head.ycor()) > (HEIGHT/2 - 1)):
        ic(snake.head.xcor(), snake.head.ycor())
        gaming = False
        scoreboard.game_over()

    # Detect collision with segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gaming = False
            scoreboard.game_over()

screen.listen()
screen.exitonclick()
