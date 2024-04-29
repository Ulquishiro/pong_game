from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

score = Scoreboard()
screen = Screen()
screen.setup(width= 800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()


ball = Ball()

r_paddle = Paddle(x=350, y=0)
l_paddle = Paddle(x=-350, y=0)


screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_moving()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_strike()
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.pad_strike()
    if ball.xcor() > -320 and ball.distance(l_paddle) < 50:
        ball.pad_strike()
    if ball.xcor() > 380:
        score.l_point()
        ball.ball_reset()
    if ball.xcor() < -380:
        score.r_point()
        ball.ball_reset()





screen.exitonclick()