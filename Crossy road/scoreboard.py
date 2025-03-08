from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(-280, 280)
        self.hideturtle()
        self.pendown()
        self.write_score_board()

    def write_score_board(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write("GAME OVER", align="center", font=FONT)

    def increase(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)
