from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0

    def menu(self):
        self.clear()
        self.penup()
        self.color("white")
        self.goto(0, 20)
        self.hideturtle()
        self.write("   THE PONG GAME\nPress space to start", False, 'center', font=("Courier", 28, 'bold'))

    def game_over(self, s):
        self.clear()
        self.goto(0, 0)
        self.write(f"The Player {s} won", False, "center", font=("Courier", 50, "normal"))

    def scores(self, side):
        if side == 1:
            self.score_1 += 1
        elif side == 2:
            self.score_2 += 1


        self.clear()
        self.penup()
        self.color("white")
        self.goto(0, 230)
        self.write(f"{self.score_1} : {self.score_2}", False, "center", font=("Courier", 50, "normal"))
        self.hideturtle()


