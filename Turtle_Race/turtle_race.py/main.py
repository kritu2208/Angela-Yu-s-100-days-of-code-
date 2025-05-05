import turtle as t
import random


screen = t.Screen()


screen.setup(width=500 , height=600)
user_bet = screen.textinput(title="Make your bet." , prompt= "Which turtle is going to win the race?Enter a color:")
colors= ["red","orange","yellow","green","blue","purple"]
y_positions = [ -70,-40,-10,40,70,100]
all_turtle = []
is_on = False

for turtle_index in range(0,6):
    tim = t.Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230 , y=y_positions[turtle_index])
    all_turtle.append(tim)
    
if user_bet:
    is_on = True
while  is_on:

    for each_turtle in all_turtle:
        x_cor = each_turtle.xcor()
        if int(x_cor) > 230:
            is_on = False
            winning_color = each_turtle.pencolor()
            if winning_color == user_bet:
                print("Your turtle win.")
            else:
                print(f"You lose.{winning_color} is the winner.")    
            

        rand_dis = random.randint(0,10)
        each_turtle.forward(rand_dis)

screen.exitonclick()
