from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")


    def move(self, direction_x, direction_y):
        new_x = self.xcor() + (10*direction_x)
        new_y = self.ycor() + (10*direction_y)
        self.goto(new_x, new_y)

