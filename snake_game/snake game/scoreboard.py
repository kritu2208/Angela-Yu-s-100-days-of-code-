from turtle import Turtle


ALIGNMENT = "Center"
FONT = "Arial"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/91812/Desktop/data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score:{self.score}  Highscore = {self.highscore}", align=ALIGNMENT , font=FONT)

    def reset_score(self):
        if self.score>self.highscore:
            self.highscore = self.score
            with open("/Users/91812/Desktop/data.txt",mode = "w") as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.update_score()    

    # def game_over(self):
    #     self.goto(x=0 , y= 0)
    #     self.write(arg="GAME OVER" , align="Center" , font="Arial")  
          

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()


