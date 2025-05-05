from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game")
screen.tracer(0)



snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="Up" , fun=snake.up)
screen.onkey(key="Down" , fun=snake.down)
screen.onkey(key="Left" , fun=snake.left)
screen.onkey(key="Right" , fun=snake.right)

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    

    #detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    x = snake.head.xcor()
    y = snake.head.ycor()
    if x > 280 or x < -280 or y > 280 or y < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    for square in snake.all_square[1:]:
        if snake.head.distance(square) < 10:
           scoreboard.reset_score()
           snake.reset_snake()   







    
        
        







screen.exitonclick()
