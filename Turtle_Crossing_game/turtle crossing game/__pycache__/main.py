import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
Car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up" , fun= player.move_forward)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    Car.create_car()
    Car.move_car()
    

    for cars in Car.all_car:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()
            

    if player.ycor()>300:
        player.goto(0 , -280)  
        Car.level_up()
        scoreboard.level_increase()

screen.exitonclick()