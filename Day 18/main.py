from turtle import Turtle, Screen

squirtle = Turtle()
squirtle.shape('turtle')
squirtle.color('black', 'orange')
squirtle.home()
squirtle.speed('fastest')

for i in range(15):
    squirtle.pendown()
    squirtle.fd(10)
    squirtle.penup()
    squirtle.fd(10)


# squirtle.penup()
# squirtle.fd(50)
# squirtle.dot(20, 'blue')
# squirtle.fd(50)
# squirtle.dot(20, 'blue')
# squirtle.fd(50)
# squirtle.dot(20, 'blue')
# squirtle.fd(50)
# squirtle.dot(20, 'blue')
# squirtle.fd(50)
# squirtle.dot(20, 'blue')
# squirtle.fd(50)







# has to happen at the end
screen = Screen()
screen.exitonclick()
