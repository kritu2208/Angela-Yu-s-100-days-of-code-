from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-250,250)
        self.update_board()
        
        


    def update_board(self):
        self.clear()
        self.write(f"Level: {self.level}" , align="left" , font=FONT)
        
    def level_increase(self):
        self.level += 1
        self.update_board()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER" , align="center", font=FONT)    