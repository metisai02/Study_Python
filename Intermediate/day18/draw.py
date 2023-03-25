
import prettytable
from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
metisai = Turtle()
screen = Screen()
metisai.shape("turtle")
metisai.color("deeppink")


def draw(number):
    angle = 360/number
    for i in range(number):
        metisai.forward(100)
        metisai.right(angle)


for r in range(3, 10):
    metisai.color(random.choice(colours))
    draw(r)

screen.exitonclick()
