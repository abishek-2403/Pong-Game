from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.move_paddle_up, key="Up")
screen.onkeypress(fun=r_paddle.move_paddle_down, key="Down")
screen.onkeypress(fun=l_paddle.move_paddle_up, key="w")
screen.onkeypress(fun=l_paddle.move_paddle_down, key="s")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.paddle_bounce()

    # r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.update_l()

    # l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.update_r()


screen.exitonclick()
