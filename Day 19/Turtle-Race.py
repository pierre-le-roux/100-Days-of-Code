from turtle import Turtle, Screen, colormode

colormode(255)

leonardo = Turtle(shape='turtle')
michelangelo = Turtle(shape='turtle')
donatello = Turtle(shape='turtle')
raphael = Turtle(shape='turtle')
skillie = Turtle(shape='turtle')

turtles = [leonardo, michelangelo, donatello, raphael, skillie]

screen = Screen()
screen.setup(width=500, height=400)

guess = screen.textinput(title='Guess',
                         prompt='Who will win the race? Enter a colour:')

print(guess)

def change_turtle(func, values):
    for i in range(len(turtles)):
        turtles[i].func(values[i])
        
turtles = {leonardo:{'colour':'blue', 'x':-255, 'y':100},
           michelangelo:{'colour':'blue', 'x':-255, 'y':50},
           donatello:{'colour':'blue', 'x':-255, 'y':0},
           raphael:{'colour':'blue', 'x':-255, 'y':-50},
           skillie:{'colour':'blue', 'x':-255, 'y':-100}}

colours = [(0, 170, 230), (255, 165, 0), (170, 27, 221), (227, 51, 28), (76, 156, 35)]
start_positions = [-225, 100, -225, 50, -225, 0, -225, -50, -225, -100]
for i in range(len(turtles)):
    turtles[i].color(colours[i])
    turtles[i].penup()
    turtles[i].goto(start_positions[2*i-1], start_positions[2*i])
        

# leonardo.color((0, 170, 230))
# michelangelo.color((255, 165, 0))
# donatello.color((170, 27, 221))
# raphael.color((227, 51, 28))
# skillie.color((76, 156, 35))

# leonardo.penup()
# michelangelo.penup()
# donatello.penup()
# raphael.penup()
# skillie.penup()

# leonardo.goto(-225, 100)
# michelangelo.goto(-225, 50)
# donatello.goto(-225, 0)
# raphael.goto(-225, -50)
# skillie.goto(-225, -100)

def who_won():
    finish_line = screen.window_width() - 20
    for turtle in turtles:
        turtle.xcor == 
    if leonardo.xcor == finish_line:
        return 'blue'
    elif 

not_finished = True
while not_finished:
    
    

screen.exitonclick()
