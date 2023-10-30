"""
    CS051P Lab Assignments: Turtle Graphics

    Name: Jayhyun Suh

    Date:   October 23, 2022

    The goal of this assignment is to give you practice working with turtle graphics
"""

from turtle import *
from random import randint, random


def draw_spirograph(n1, n2, pc, fc):
    """
    draws a spiral like shape until it reaches the starting point. Then fills certain areas of the shape
    :param n1: length traveled in the loop
    :param n2: degrees turned in the loop
    :param pc: pencolor
    :param fc: fill color
    :return:
    """
    pencolor(pc)
    fillcolor(fc)
    begin_fill()
    while True:
        forward(n1)
        left(n2)
        if abs(pos()) < 1:
            break
    end_fill()
    done()


def draw_triangle(length):
    """
    Draws an equilateral triangle with each side being length and a pencolor of color
    :param: (int) length of the sides
    :param: (str) color of the lines
    draws an equilateral triangle of length and color
    """
    # goes forward and turns left 120 degrees 3 times
    for _ in range(3):
        forward(length)
        left(120)


def draw_hexagon_triangle(length, color):
    """
    Draws a triangle 6 times to create a hexagon
    :param length: (int) length of sides
    :param color: (str) color of the lines
    """
    # draws a triangle six times, after each triangle rotates 60 degrees to the left
    for _ in range(6):
        draw_triangle(length, color)
        left(60)


def main_part1():
    """
    Creates three hexagons from the draw_hexagon_triangle function side by side with different colors
    """
    length = 50
    draw_hexagon_triangle(length, "green")
    penup()
    forward(2 * length)
    pendown()
    draw_hexagon_triangle(length, "blue")
    penup()
    forward(2 * length)
    pendown()
    draw_hexagon_triangle(length, "red")
    done()


def draw_polygon(n, length):
    """
    Draws a loop of lines adjusted by angles to create a polygon based on the given number of sides and length
    :param n: (int) number of sides
    :param length: (int) length of each side
    """
    angle = 360 / n
    # for number of sides, turtle goes forward and turns right
    for _ in range(n):
        forward(length)
        right(angle)


def draw_spiral(increment, deg, n):
    """
    Creates a spiral consisting of straight lines that increasingly grow longer and ends at the range of n
    :param increment: (int) the amount the length increases each time
    :param deg: (int) the degree in which the spiral turns each time
    :param n: (int) the amount of spirals created
    """
    counter = 1
    # for the range in n, goes forward increment that increases by itself each time and turns right a certain degree
    for x in range(n):
        forward(increment * counter)
        right(deg)
        counter += 1


def rotate_repeat(k, n, length, drawing):
    """
    Draws a shape given by a function repeatedly. Each time rotates a certain degree
    :param k: (int) number of shapes function draws
    :param n: (int) number of sides in the shape
    :param length: (int) length of the sides in the shape
    :param drawing: (function) a drawing function
    """
    # for the range of k, draws a given shape with n sides and length, and rotates a degree of 360 / k
    for x in range(k):
        drawing(n, length)
        right(360 / k)


def draw_circle():
    """
    helper function that draws a circle and fills it.
    """
    begin_fill()
    circle(10)
    end_fill()


def random_circle():
    """
    Draws a random circle somewhere on the screen. Based on the location on the x-axis, the shade of red is different
    """
    # color is determined by rgb values
    colormode(255)
    # turtle starts in the middle of the screen so the height and width divided by 2 gets the range of the screen
    x = window_width() // 2
    y = window_height() // 2
    random_x = randint(-x, x)
    random_y = randint(-y, y)
    # penup() so it doesn't draw a line to the coordinates
    penup()
    goto(random_x, random_y)
    pendown()
    # different color filled circles based on x-value of the location
    if random_x < -450:
        fillcolor(220, 28, 1)
        draw_circle()
    elif -450 < random_x < -150:
        fillcolor(234, 76, 70)
        draw_circle()
    elif -150 < random_x < 150:
        fillcolor(240, 116, 112)
        draw_circle()
    elif 150 < random_x < 450:
        fillcolor(241, 149, 155)
        draw_circle()
    else:
        fillcolor(246, 189, 192)
        draw_circle()


def main():
    """
    draws an image consisting of polygons, spirals, rotated shapes and many circles
    """
    # pentagons
    # fill a medium-sized square with yellow
    fillcolor("yellow")
    begin_fill()
    draw_polygon(4, 200)
    end_fill()
    # draw a small square on the top left of the previous square
    fillcolor("purple")
    begin_fill()
    draw_polygon(4, 20)
    end_fill()
    penup()
    # draw a big triangle rotated 30 degrees
    goto(-250, 300)
    right(30)
    pendown()
    draw_polygon(3, 900)
    penup()
    # go to roughly the middle of the medium square and draw a 20 sided pentagon
    begin_fill()
    goto(100, -100)
    pendown()
    draw_polygon(20, 5)
    end_fill()

    # spirals
    # draw a blue spiral that looks like pentagons and fill the areas that touch with blue
    pencolor("blue")
    fillcolor("blue")
    begin_fill()
    draw_spiral(10, 50, 30)
    end_fill()
    penup()
    # go to the start and draw a green spiral of that ends up like a wing
    goto(100, -100)
    pendown()
    pencolor("green")
    draw_spiral(20, 177, 30)
    penup()
    # go to the center and create an orange spiral that looks like pentagons
    goto(100, -100)
    pendown()
    pencolor("orange")
    fillcolor("orange")
    begin_fill()
    draw_spiral(15, 275, 50)
    end_fill()

    # rotate
    # draw 8 octagons and fill parts of it black on the top left side of the screen
    penup()
    pencolor("red")
    goto(-350, 250)
    pendown()
    fillcolor("black")
    begin_fill()
    rotate_repeat(8, 8, 70, draw_polygon)
    end_fill()

    # circles
    # draw 25 circles from random_circle function
    for _ in range(25):
        random_circle()

    done()


if __name__ == '__main__':
    # main_part1()  # comment this out after you check-in for part 1
    main()  # uncomment this after you check-in for part 1

"""
def drawc(x, y, radius):
    z = 0
    if radius <= 50:
        penup()
        goto(x, y - radius)
        pendown()
        circle(radius)
        z = 1
    else:
        z += drawc(x + radius / 2, y, radius / 2)
        z += drawc(x - radius / 2, y, radius / 2)
        z += drawc(x, y +radius / 2, radius / 2)
        z += drawc(x, y - radius / 2, radius / 2)

    return z
print(drawc(0, 0, 200))
done()
"""