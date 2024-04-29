from turtle import Turtle
import random

angle = random.randint(0, 360)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition(0, 0)
        self.x_move = 10
        self.y_move = 10

    def ball_moving(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_strike(self):
        self.y_move *= -1

    def pad_strike(self):
        self.x_move *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.pad_strike()







