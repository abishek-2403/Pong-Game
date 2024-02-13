from turtle import Turtle

Y = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.08

    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.color("white")

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.08
        self.paddle_bounce()

    def bounce(self):
        self.move_y *= -1

    def paddle_bounce(self):
        self.move_x *= -1
        self.move_speed *= 0.9
