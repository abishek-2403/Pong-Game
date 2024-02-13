from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_point = 0
        self.r_point = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 250)
        self.write(f"{self.r_point}", align="center", font=("Arial", 30, "normal"))
        self.goto(-100, 250)
        self.write(f"{self.l_point}", align="center", font=("Arial", 30, "normal"))

    def update_r(self):
        self.r_point += 1
        self.update_score()

    def update_l(self):
        self.l_point += 1
        self.update_score()
