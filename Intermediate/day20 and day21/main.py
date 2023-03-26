from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBroad

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


screen = Screen()
screen.setup(width=700, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBroad()
screen.listen()

screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


end_game = False
while not end_game:
    screen.update()
    time.sleep(0.07)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        for i in snake.snake_b:
            i.color(random.choice(colours))
        score.increse()
    if snake.head.xcor() < -330 or snake.head.xcor() > 330 or snake.head.ycor() < -230 or snake.head.ycor() > 230:
        end_game = True
        score.game_over()


screen.exitonclick()
