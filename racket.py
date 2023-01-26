from turtle import Turtle

class Racket:

    def __init__(self):
        self.segments_racket = []
        self.create_racket()
        self.racket1 = self.segments_racket[0]
        self.racket2 = self.segments_racket[1]

    def create_racket(self):
        X = 350
        for racket in range(2):
            racket = Turtle()
            racket.penup()
            racket.shape("square")
            racket.color("white")
            racket.shapesize(stretch_wid=5, stretch_len=1)
            racket.goto(X, 0)
            X -= 700
            self.segments_racket.append(racket)

    def down1(self):
        new_Y = self.racket1.ycor() - 20
        self.racket1.goto(self.racket1.xcor(), new_Y)

    def up1(self):
        new_Y = self.racket1.ycor() + 20
        self.racket1.goto(self.racket1.xcor(), new_Y)

    def down2(self):
        new_Y = self.racket2.ycor() - 20
        self.racket2.goto(self.racket2.xcor(), new_Y)

    def up2(self):
        new_Y = self.racket2.ycor() + 20
        self.racket2.goto(self.racket2.xcor(), new_Y)
