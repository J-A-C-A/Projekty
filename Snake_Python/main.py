
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from turtle import Screen

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

starting_positions = [(0,0),(-20,0),(20,0)]
segments = []

snake = Snake()
food =  Food()
s_b = ScoreBoard()
screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        s_b.increase()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        s_b.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            s_b.reset()
            snake.reset()


screen.exitonclick()
