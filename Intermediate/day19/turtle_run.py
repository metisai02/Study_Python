from turtle import Turtle, Screen
import random

screen = Screen()
user = screen.textinput("NIM", "Name of first player:")
screen.setup(width=500, height=400)
color = ['red', 'blue', 'black', 'pink', 'green']
character = []

for i in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    character.append(new_turtle)
    character[i].color(color[i])
    character[i].penup()
    character[i].goto(x=-230, y=(-60 + i*30))
eng_game = False

while not eng_game:
    for i in character:
        if i.xcor() > 230 :
            eng_game = True
            if i.xcor() == user:
                print("you win")
            else:
                print("you loose")
            print(f"turtle {i.pencolor()} win")
        i.forward(random.randint(0,10)) 

screen.exitonclick()
