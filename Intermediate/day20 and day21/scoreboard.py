from turtle import Turtle


class ScoreBroad(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 210)

        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align='center',
                   font=("Arial", 24, "normal"))
    def increse(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center',
                   font=("Arial", 24, "normal"))
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center',
                   font=("Arial", 24, "normal"))