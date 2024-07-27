from turtle import Turtle
class Ball(Turtle):
    def __init__(self, STARTING_POSITION=(0, 0)):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.penup()
        self.goto(STARTING_POSITION)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        '''Bouncing off the top surface'''
        self.y_move *= -1

    def x_bounce(self):
        '''Bouncing of the bat'''
        self.x_move *= -1
