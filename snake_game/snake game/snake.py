from turtle import Turtle
STARTING_POSITION = [(0,0) , (-20,0) , (-40,0)]
XCORD = [ -20 ,0 , 20]
MOVE_DISTANCE = 20
UP = 90
DOWN =270
LEFT = 180
RIGHT = 0

class Snake:


    def __init__(self):
        self.all_square = []
        self.create_snake()
        self.head = self.all_square[0] 
        

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_square(position)

    def reset_snake(self):
        for square in self.all_square:
            square.goto(1000,1000)
        self.all_square.clear()
        self.create_snake()
        self.head = self.all_square[0]



    def add_square(self , positions):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("white")
        tim.goto(positions)
            
        self.all_square.append(tim)

    def extend(self):
        self.add_square(self.all_square[-1].position())


    def snake_move(self):
             
    
        for new_square in range(len(self.all_square)-1 , 0 , -1):
            new_x = self.all_square[new_square - 1].xcor()
            new_y = self.all_square[new_square - 1].ycor()
            self.all_square[new_square].goto( new_x,new_y)
        self.head.forward(MOVE_DISTANCE)    
          


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN) 
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)   

           
             