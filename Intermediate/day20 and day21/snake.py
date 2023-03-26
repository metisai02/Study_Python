from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DEFAULT = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_b = []
        self.create_snake()
        self.head = self.snake_b[0]
      #  self.color('pink')

    def create_snake(self):
        for position in STARTING_POSITION:
            snake_length = Turtle(shape="square")
            snake_length.up()
            snake_length.color("deeppink")
            snake_length.goto(position)
            self.snake_b.append(snake_length)

    def move(self):
        for seg in range(len(self.snake_b)-1, 0, -1):
            x_old = self.snake_b[seg-1].xcor()
            y_old = self.snake_b[seg-1].ycor()
            self.snake_b[seg].goto(x_old, y_old)
        self.snake_b[0].forward(MOVE_DEFAULT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
