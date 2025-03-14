from turtle import Screen
import turtle as t
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

R_PADDLE_POSITION = (350,0)
L_PADDLE_POSITION = (-350,0)

ball = Ball()
scoreboard = Scoreboard()


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle(R_PADDLE_POSITION)
l_paddle = Paddle(L_PADDLE_POSITION)


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on: 
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    ## detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
            # need to bounce()
            ball.bounce_y()

    ## detect collision with the r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
            ball.bounce_x()
            
    
    ## detect when r_paddle missed
    if ball.xcor() > 380:
           ball.reset_position()
           scoreboard.l_point()

    ## detect whenn l_paddle missed
    if ball.xcor() < -380: 
           ball.reset_position()
           scoreboard.r_point()

           
           
screen.exitonclick()

