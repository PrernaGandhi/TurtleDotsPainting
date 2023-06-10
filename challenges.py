import random
import turtle
from turtle import Turtle, Screen

angles = [0, 90, 180, 270]
tim = Turtle()


def draw_dashed_line():
    for i in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

    # screen = Screen()
    # screen.exitonclick()


def draw_square():
    tim.shape("classic")

    for i in range(4):
        tim.right(90)
        tim.forward(200)


def get_random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


def draw_shapes():
    turtle.colormode(255)
    for side in range(3, 11):
        angle = 360 / side
        tim.color(get_random_color())
        for _ in range(side):
            tim.forward(100)
            tim.right(angle)


def draw_random_walk():
    tim.speed(10)
    tim.pensize(15)
    # this turtle.colormode(255) is required for
    # color to work with r, g, b color
    turtle.colormode(255)
    for _ in range(200):
        tim.color(get_random_color())
        tim.setheading(random.choice(angles))
        tim.forward(30)


def draw_spirograph():
    turtle.colormode(255)
    # tim.pensize(10)
    tim.speed("fastest")
    angle = 0
    while angle <= 360:
        tim.color(get_random_color())
        tim.circle(100)
        tim.setheading(angle)
        angle += 5


# draw_square()
# draw_dashed_line()
# draw_shapes()
# draw_random_walk()
# draw_spirograph()
