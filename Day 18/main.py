from turtle import Turtle, Screen

squirtle = Turtle()
squirtle.shape('turtle')
squirtle.color('black', 'orange')
squirtle.home()
squirtle.speed('fastest')

for distance in range(200, -5, -5):
    squirtle.fd(distance)
    squirtle.left(90)
    squirtle.fd(distance)
    squirtle.left(90)
    squirtle.fd(distance)
    squirtle.left(90)
    squirtle.fd(distance)
for distance in range(0, 205, 5):
    squirtle.fd(distance)
    squirtle.right(90)
    squirtle.fd(distance)
    squirtle.right(90)
    squirtle.fd(distance)
    squirtle.right(90)
    squirtle.fd(distance)
for distance in range(200, -5, -5):
    squirtle.fd(distance)
    squirtle.right(90)
    squirtle.fd(distance)
    squirtle.right(90)
    squirtle.fd(distance)
    squirtle.right(90)
    squirtle.fd(distance)
for distance in range(0, 205, 5):
    squirtle.fd(distance)
    squirtle.left(90)
    squirtle.fd(distance)
    squirtle.left(90)
    squirtle.fd(distance)
    squirtle.left(90)
    squirtle.fd(distance)


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
