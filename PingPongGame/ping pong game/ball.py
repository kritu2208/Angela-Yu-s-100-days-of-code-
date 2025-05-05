from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1
        
    def ball_move(self):

        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x,new_y)
        



    def ball_bounce_y(self):
        self.move_y *= -1
        self.ball_move()
        self.move_speed *= 0.9

    def ball_bounce_x(self):
        self.move_x *= -1
        self.ball_move()    
        self.move_speed *= 0.9      