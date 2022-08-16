from turtle import Turtle, Screen


shelly = Turtle()
screen = Screen()


def move_forwards():
    shelly.forward(10)


def move_backwards():
    shelly.backward(10)


def turn_right():
    shelly.right(10)


def turn_left():
    shelly.left(10)


def clear():
    shelly.clear()
    shelly.penup()
    shelly.home()
    shelly.pendown()


def main():
    screen.listen()
    screen.onkeypress(key='w', fun=move_forwards)
    screen.onkeypress(key='s', fun=move_backwards)
    screen.onkeypress(key='a', fun=turn_left)
    screen.onkeypress(key='d', fun=turn_right)
    screen.onkey(key='c', fun=clear)
    screen.exitonclick()


if __name__ == '__main__':
    main()
