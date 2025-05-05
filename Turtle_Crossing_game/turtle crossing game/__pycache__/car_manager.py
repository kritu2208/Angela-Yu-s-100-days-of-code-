from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self) -> None:
        
        
        
        self.all_car = []
        self.car_speed = MOVE_INCREMENT


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1 , stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250,250)
        
            new_car.goto(300,new_y)
            self.all_car.append(new_car)
            



    def move_car(self):
        for cars in self.all_car:
            cars.backward(self.car_speed)   


    def level_up(self):
        self.car_speed += MOVE_INCREMENT         
