from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.pendown()
        self.write_score_board()

    def write_score_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 18, "bold"))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt" , mode = "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.write_score_board()


    # def game_over(self):
    #     self.penup()
    #     self.goto(0,0)
    #     self.pendown()
    #     self.write("GAME OVER" , align="center" , font=("Arial", 18, "bold"))

    def increase(self):
        self.score += 1
        self.write_score_board()
