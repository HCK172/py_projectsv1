from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # define our score board
        self.color("white")
        self.penup()
        self.hideturtle()
        # attribute for the score
        self.lscore = 0
        self.rscore = 0
        self.update_scoreboard()
        

    def update_scoreboard(self): 
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        self.lscore += 1
        self.update_scoreboard()
    
    def r_point(self):
        self.rscore += 1 
        self.update_scoreboard()