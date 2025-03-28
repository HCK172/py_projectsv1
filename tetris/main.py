from turtle import Turtle, Screen
import time
import random 

screen = Screen()
screen.setup(width=300, height=600)
screen.title("Tretis")
screen.tracer(0)


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()



screen.exitonclick()
