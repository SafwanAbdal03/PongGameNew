from turtle import Turtle

class TennisBat(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def GotoPosition(self, STARTING_POSITION):
        self.goto(STARTING_POSITION)

    def Move_Down(self):
        if self.ycor() > -150: #preventing the bat from going out of the screen
            self.sety(self.ycor() - 20)

    def Move_Up(self):
        if self.ycor() < 150:
            self.sety(self.ycor() + 20)