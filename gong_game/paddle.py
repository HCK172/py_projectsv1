from turtle import Turtle
# turtle default size (20,20)

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.move = 22
    

    def go_up(self):
            
        if self.ycor() > 235:
               pass
        else:     
            new_y = self.ycor() + self.move
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() < -235: 
            pass
        else:
            new_y = self.ycor() - self.move
            self.goto(self.xcor(), new_y)
