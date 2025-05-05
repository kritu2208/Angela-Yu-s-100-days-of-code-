from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = scoreboard()

screen.listen()
screen.onkey(key= "Up" , fun=r_paddle.move_up)
screen.onkey(key="Down" , fun=r_paddle.move_down)
screen.onkey(key= "w" , fun=l_paddle.move_up)
screen.onkey(key="s" , fun=l_paddle.move_down)

def ball_moving():
    ball.ball_move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce_y()
        

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.ball_bounce_x()
        

   
           

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball_moving()
    
    if ball.xcor()>380 : 
        scoreboard.l_gain_point()
        ball.goto(0,0)
        ball.move_speed = 0.1
        ball_moving()
        

    if ball.xcor()<-380:  
        scoreboard.r_gain_point()  
        ball.goto(0,0)
        ball.move_speed = 0.1
        ball_moving()
        
    












screen.exitonclick()