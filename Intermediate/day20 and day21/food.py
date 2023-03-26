from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.color("pink")
        self.speed("fastest")

        random_x = random.randint(-330, 330)
        random_y = random.randint(-230, 230)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-330, 330)
        random_y = random.randint(-230, 230)
        self.goto(random_x, random_y)
