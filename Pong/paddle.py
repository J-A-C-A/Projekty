from turtle import Turtle
class Paddle(Turtle):
    def __init__(self , x_pos , y_pos):
        super().__init__()
        self.shape("square")
        self.showturtle()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.penup()
        self.goto(x_pos, y_pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor() , new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
