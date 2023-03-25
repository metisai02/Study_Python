import prettytable
from turtle import Turtle, Screen
import turtle as t

import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
metisai = Turtle()
screen = Screen()
metisai.shape("turtle")
metisai.color("deeppink")
#metisai.pensize(20)
#metisai.speed(10)
t.colormode(255)
direction = [0, 90, 180, 270]


def draw(number):
    angle = 360/number
    for i in range(number):
        metisai.forward(100)
        metisai.right(angle)


def walk_random():
    metisai.forward(50)
    metisai.right(random.choice(direction))


def random_color():
    r = (random.randint(0, 255))
    g = (random.randint(0, 255))
    b = (random.randint(0, 255))

    color = (r,g,b)
    return color


# metisai.write("Home = ", True, align="center")
# metisai.write((0,0), True)
metisai.circle(50)

screen.exitonclick()
