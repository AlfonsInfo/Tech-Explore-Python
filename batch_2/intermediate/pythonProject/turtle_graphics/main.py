import random
import turtle
from turtle import Turtle, Screen
import heroes


# from Turtle import *
screen = Screen()
screen.colormode(255)
def draw_square(tim):
    for _ in range(4):
        tim.forward(100)
        tim.left(90)


def draw_dashed_line(tim, distance, loop):
    for _ in range(loop):
        tim.forward(distance)
        tim.penup()
        tim.forward(distance)
        tim.pendown()


def draw_triangle(tim):
    for _ in range(3):
        tim.forward(100)
        tim.left(angle=120)


def draw_pentagon(tim):
    for _ in range(5):
        tim.forward(100)
        tim.left(angle=72)


def draw_two_dimensional_figure(sisi):
    sudut = 360 / sisi
    for _ in range(sisi):
        tim.forward(100)
        tim.left(sudut)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_rgb = (r, g, b)
    return random_rgb


def draw_random_walk():
    colours = random_color()
    directions = [0, 90, 180, 270]
    tim.pensize(15)
    for _ in range(200):
        tim.color(colours)
        tim.forward(30)
        tim.setheading(random.choice(directions))


def draw_spirograph(size_of_gaph):
    for _ in range(int(360 / size_of_gaph)):
        colours = random_color()
        tim.circle(50)
        tim.color(colours)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gaph)


tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed("fastest")


draw_spirograph(10)
# draw_random_walk()
# draw_square(tim)
# draw_dashed_line(tim,10,15)
# draw_triangle(tim)
# tim.color("blue")
# draw_square(tim)
# draw_pentagon(tim)

# for i in range(3,20):
#     draw_two_dimensional_figure(i)



screen.exitonclick()
