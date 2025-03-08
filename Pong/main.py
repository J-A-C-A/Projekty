import time
from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=900 , height=600)
screen.bgcolor("black")
screen.tracer(0)


screen.title("The Pong Game")
r_pad = Paddle(350,0)
l_pad = Paddle(-350,0)
ball = Ball()
s_b = ScoreBoard()
screen.listen()


screen.onkey(fun= r_pad.up , key="Up")
screen.onkey(fun= r_pad.down , key="Down")

screen.onkey(fun= l_pad.up , key="w")
screen.onkey(fun= l_pad.down , key="s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_pad) < 50 and ball.xcor() > 320 or ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        s_b.increase_left()
        ball.reset_position()
    if ball.xcor() < -380:
        s_b.increase_right()
        ball.reset_position()

screen.exitonclick()

