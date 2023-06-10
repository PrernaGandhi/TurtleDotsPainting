# import colorgram
#
# colors = colorgram.extract('image.jpg', 1010)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_colors.append(rgb_color)
#
# print(rgb_colors)

import turtle
import random

colors_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106),
               (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
               (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31),
               (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113),
               (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124),
               (153, 202, 227), (48, 69, 71), (131, 128, 121)]

tim = turtle.Turtle()
turtle.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
x_cor = tim.xcor()
y_cor = tim.ycor()

for dots in range(101):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)
    if dots % 10 == 0:
        tim.setx(x_cor)
        tim.sety(y_cor + 5 * dots)

screen = turtle.Screen()
screen.exitonclick()
#print(tim)