import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("The Turtle Street Game")

p = Player()
c_m = CarManager()
s_b = Scoreboard()

screen.listen()
screen.onkey(fun= p.move , key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    c_m.create_car()
    c_m.move()

    if p.ycor() >= 280:
        s_b.increase()
        p.go_to_start_line()
        c_m.increase_speed()
        time.sleep(0.5)

    for car in c_m.all_cars:
        if p.distance(car) < 30:
            s_b.game_over()
            game_is_on = False


screen.exitonclick()