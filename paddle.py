from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(self.position)

    def move_paddle_up(self):
        y = self.ycor() + 50
        x = self.xcor()
        self.goto(x, y=y)

    def move_paddle_down(self):
        y = self.ycor() - 50
        x = self.xcor()
        self.goto(x, y=y)
