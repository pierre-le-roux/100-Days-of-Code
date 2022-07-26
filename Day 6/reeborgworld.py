# functions

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def walk_along_wall():
    move()
    while wall_on_right():
        if front_is_clear():
            move()
        else:
            break

def jump():
    turn_left()
    walk_along_wall()
    turn_right()
    move()
    turn_right()
    walk_along_wall()
    turn_left()


# Hurdle 1 (https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)

while not at_goal():
    move()
    jump()

# Hurdle 3 (https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json)

while not at_goal():

    while front_is_clear():
        if at_goal():
            break
        move()

    while wall_in_front():
        jump()


# Hurdle 4 (http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json)

while not at_goal():

    while front_is_clear():
        if at_goal():
            break
        move()

    while wall_in_front():
        jump()

# Maze (https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)

while not at_goal():

    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_right()
        move()