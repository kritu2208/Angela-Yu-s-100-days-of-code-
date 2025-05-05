import turtle as t

tim = t.Turtle()
screen = t.Screen()

screen.listen()

def move_forward():
    tim.forward(50)

def move_backward():
    tim.backward(50)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def turn_left():
    tim.left(45)  

def turn_right():
    tim.right(45)           

screen.onkey(key="w" , fun= move_forward) 
screen.onkey(key="s" , fun=move_backward) 
screen.onkey(key="a" , fun=turn_left) 
screen.onkey(key="d" , fun=turn_right)  
screen.onkey(key="c" , fun=clear_drawing) 







screen.exitonclick()