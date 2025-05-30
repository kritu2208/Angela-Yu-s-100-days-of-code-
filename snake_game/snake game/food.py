from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5 , stretch_len=0.5)
        self.penup()
        

    def refresh(self):
        rand= random.randint(-280 , 280)
        self.goto(x = rand , y = rand)