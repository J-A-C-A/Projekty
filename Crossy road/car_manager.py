from turtle import Turtle
import random
COLORS = ["red", "orange", "pink", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(320,320)
        self.hideturtle()
        self.all_cars = []
        self.starting_speed = STARTING_MOVE_DISTANCE
        self.speed_increment = MOVE_INCREMENT

    def move(self):
        for car in self.all_cars:
            car.forward(self.starting_speed)

    def increase_speed(self):
        self.starting_speed += self.speed_increment

    def create_car(self):
        rand_chance = random.randint(1,6)
        if rand_chance == 1:
            new_car = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid= 1 , stretch_len= 2)
            new_car.setheading(180)
            new_car.penup()
            new_car.goto(300, random.randint(-250,250))
            self.all_cars.append(new_car)
