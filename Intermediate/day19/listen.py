
from turtle import Turtle, Screen

metisai = Turtle()

screen = Screen()


def forward():
    metisai.forward(20)
def goback():
    metisai.back(10)
def turnleft():
    metisai.left(10)
def turnright():
    metisai.right(10)

screen.listen()
screen.onkey(fun=forward, key="w")
screen.onkey(fun=goback, key="s")
screen.onkey(fun=turnleft, key="a")
screen.onkey(fun=turnright, key="d")
screen.exitonclick()
