from turtle import Turtle, Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on: 
    time.sleep(0.05)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    ## detect collsion with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False 
            scoreboard.game_over()
            

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()