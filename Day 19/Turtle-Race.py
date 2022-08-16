from random import randint
from turtle import Turtle, Screen, colormode

colormode(255)

leonardo = Turtle(shape='turtle')
michelangelo = Turtle(shape='turtle')
donatello = Turtle(shape='turtle')
raphael = Turtle(shape='turtle')
skillie = Turtle(shape='turtle')

turtles = {leonardo: {'colour': 'blue', 'x': -200, 'y': 100},
           michelangelo: {'colour': 'orange', 'x': -200, 'y': 50},
           donatello: {'colour': 'purple', 'x': -200, 'y': 0},
           raphael: {'colour': 'red', 'x': -200, 'y': -50},
           skillie: {'colour': 'green', 'x': -200, 'y': -100}}


screen = Screen()
screen.setup(width=500, height=400)


def get_guess():
    return screen.textinput(title='Guess',
                            prompt='Who will win the race? Enter a colour:')


def initialise_game(finish_line):
    line = Turtle(visible=False)
    line.penup()
    y_top = turtles[list(turtles.keys())[0]]['y'] + 50
    y_bot = turtles[list(turtles.keys())[-1]]['y'] - 50
    line.goto(finish_line, y_top)
    line.pendown()
    line.goto(finish_line, y_bot)

    for turtle in turtles.keys():
        turtle.speed('fastest')
        turtle.color(turtles[turtle]['colour'])
        turtle.penup()
        turtle.goto(turtles[turtle]['x'], turtles[turtle]['y'])


def who_won(guess, finish_line):
    for turtle in turtles.keys():
        if turtle.xcor() >= finish_line:
            if guess == turtles[turtle]['colour']:
                print(f'Congrats the {guess} turtle won!')
            else:
                print(f"Sorry the {turtles[turtle]['colour']} turtle won,",
                      f"and you chose {guess}")
            return True


def random_movement():
    for turtle in turtles.keys():
        turtle.forward(randint(0, 25))


def main():
    not_finished = True
    guess = get_guess()
    finish_line = screen.window_width()/2 - 25
    initialise_game(finish_line)
    while not_finished:
        random_movement()
        if who_won(guess, finish_line):
            not_finished = False

    screen.listen()
    screen.onkey('c', main())

    screen.exitonclick()


if __name__ == '__main__':
    main()
