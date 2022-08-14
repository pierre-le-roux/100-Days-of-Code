from svg_turtle import SvgTurtle
from random import random, seed, choice
from colorgram import extract
import os
from icecream import ic

CURRENT_DIR = os.path.dirname(__file__)
IMAGE_PATH = os.path.join(CURRENT_DIR, 'image.jpg')


class pen(SvgTurtle):

    def __init__(self, width, height) -> None:
        super().__init__(width, height)
        self.screen.screensize(width, height)
        self.width = width
        self.height = height
        self.speed('fastest')
        self.start_x = 0
        self.start_y = 0

    def extract_image_colours(self, path_to_image, rows, columns):
        self.image_colours = list(extract(path_to_image, (rows-1)*(columns-1)))

        ic(self.image_colours)

    def window_grid(self, columns, rows):
        self.x_space = self.width/columns
        self.y_space = self.height/rows

        ic(self.x_space, self.y_space)

        self.start_x -= self.width/2 - self.x_space
        self.start_y += self.height/2 - self.y_space

        ic(self.start_x, self.start_y)

        self.x_col = columns-1
        self.y_rows = rows-1

    def even_grid(self, columns, rows, distance):
        width = columns*distance
        height = rows*distance

        self.x_space = distance
        self.y_space = distance

        ic(self.x_space, self.y_space)

        self.start_x -= width/2 - self.x_space
        self.start_y += height/2 - self.y_space

        ic(self.start_x, self.start_y)

        self.x_col = columns-1
        self.y_rows = rows-1

    def change_color(self, is_random=True):
        if is_random:
            R = random()
            G = random()
            B = random()
        else:
            light_colour = True
            while light_colour:
                colour = choice(self.image_colours).rgb
                R = colour.r * (1/255)
                G = colour.g * (1/255)
                B = colour.b * (1/255)
                if R > (240 * (1/255)) and \
                   G > (240 * (1/255)) and \
                   B > (240 * (1/255)):
                    light_colour = True
                else:
                    light_colour = False
        ic(R, G, B)

        return (R, G, B)

    def draw_grid(self, columns, rows, distance=None):
        if distance:
            self.even_grid(columns, rows, distance)
        else:
            self.window_grid(columns, rows)

        self.extract_image_colours(IMAGE_PATH, columns, rows)

        self.penup()
        self.goto(self.start_x, self.start_y)

        for y in range(self.y_rows):
            for x in range(self.x_col):
                self.goto(self.start_x + self.x_space*x,
                          self.start_y - self.y_space*y)
                self.dot(20, self.change_color(False))

    def write_file(self, filename):
        self.save_as(os.path.join(CURRENT_DIR, filename))


def main():
    ic.disable()
    for s_nr in range(1, 1001):
        seed(s_nr)
        squirtle = pen(500, 500)
        squirtle.hideturtle()
        squirtle.draw_grid(10, 10)
        squirtle.write_file(f'art_{s_nr}.svg')


if __name__ == '__main__':
    main()
