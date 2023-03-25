

import prettytable

from turtle import Turtle, Screen

metisai = Turtle()
screen = Screen()
metisai.shape("turtle")
metisai.color("deeppink")

for i in range(10):   
    metisai.forward(10)
    metisai.up()
    metisai.forward(10)
    metisai.down()

screen.exitonclick()