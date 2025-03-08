STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.go_to_start_line()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start_line(self):
        self.goto(STARTING_POSITION)