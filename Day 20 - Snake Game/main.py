from turtle import Screen
from snake import Snake
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()

gaming = True
while gaming:
    screen.update()
    sleep(0.2)

    snake.move()




screen.listen()
screen.exitonclick()
