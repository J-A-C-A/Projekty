from turtle import Turtle , Screen
import random


screen = Screen()
is_race_on = False
screen.setup(width=500 , height=400)
user_bet = screen.textinput(title="Choose color of your turtle",prompt="Which turtle will win the race? Enter a color: ")
colors=["red","blue","orange","black","green","purple"]

x_start = -230
y_start = -60
all_turtles = []
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.teleport(x= x_start ,y= y_start)
    y_start += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The winning turtle is {winning_color} turtle!")
                is_race_on = False
            else:
                print(f"You've lose! The winning turtle is {winning_color} turtle!")
                is_race_on = False
        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()






