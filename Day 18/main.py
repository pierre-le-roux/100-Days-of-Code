from turtle import Turtle, Screen, colormode
from random import randint, seed, choice
from colorgram import extract
import os
from icecream import ic

seed(1)
colormode(255)
SCREEN = Screen()
IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'image.jpg')


class pen(Turtle):

    def __init__(self, shape: str = 'classic',
                 undobuffersize: int = 0, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.speed('fastest')
        self.start_x = 0
        self.start_y = 0

    def extract_image_colours(self, path_to_image):
        self.image_colours = list(extract(path_to_image, 20))
        ic(self.image_colours)

    def grid(self, columns, rows):
        width = SCREEN.window_width()
        height = SCREEN.window_height()

        self.x_space = width/columns
        self.y_space = height/rows

        ic(self.x_space, self.y_space)

        self.start_x -= width/2 - self.x_space
        self.start_y += height/2 - self.y_space

        ic(self.start_x, self.start_y)

        self.x_col = columns-1
        self.y_rows = rows-1

    def change_color(self, is_random=True):
        if is_random:
            R = randint(0, 255)
            G = randint(0, 255)
            B = randint(0, 255)
        else:
            colour = choice(self.image_colours).rgb
            R = colour.r
            G = colour.g
            B = colour.b
        ic(R, G, B)

        self.color((R, G, B))

    def draw_grid(self, columns, rows):
        self.grid(columns, rows)
        self.extract_image_colours(IMAGE_PATH)

        self.penup()
        self.goto(self.start_x, self.start_y)

        for y in range(self.y_rows):
            for x in range(self.x_col):
                self.goto(self.start_x + self.x_space*x,
                          self.start_y - self.y_space*y)
                self.change_color(False)
                self.dot(15)


def main():
    ic.disable()
    squirtle = pen()
    squirtle.draw_grid(12, 9)

    SCREEN.exitonclick()


if __name__ == '__main__':
    main()
