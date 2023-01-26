from turtle import Screen
from racket import Racket
from ball import Ball
import time
from scoreboard import Scoreboard

# SCREEN
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

# VARIABLES
racket = Racket()
ball = Ball()
score = Scoreboard()

def start_game():
    # START THE GAME
    is_on = True

    # THOSE VARIABLES ARE USED TO CONTROL THE GAME FUNCTIONALITY
    X = 1
    Y = 1
    time_speed = 0.1
    score.scores(0)

    while is_on:
        screen.update()
        time.sleep(time_speed)
        ball.move(X, Y)

        # CHANGE BALL'S DIRECTION
        if ball.ycor() > 280 or ball.ycor() < -280:
            Y *= -1
            ball.move(X, Y)

        if ball.distance(racket.racket1) < 50 and ball.xcor() > 320 or ball.distance(
                racket.racket2) < 50 and ball.xcor() < -320:
            X *= -1
            ball.move(X, Y)
            time_speed *= 0.75

        if ball.xcor() < -380:
            ball.goto(0, 0)
            X *= -1
            score.scores(2)
            ball.move(X, Y)
            time_speed = 0.1

        if ball.xcor() > 380:
            ball.goto(0, 0)
            X *= -1
            score.scores(1)
            ball.move(X, Y)
            time_speed = 0.1

        if score.score_2 == 5:
            score.game_over(2)
            is_on = False
            time.sleep(3)
            screen.bye()
        elif score.score_1 == 5:
            score.game_over(1)
            is_on = False
            time.sleep(3)
            screen.bye()


# KEYS
screen.listen()
screen.onkeypress(racket.up1, "Up")
screen.onkeypress(racket.down1, "Down")
screen.onkeypress(racket.up2, "w")
screen.onkeypress(racket.down2, "s")
screen.onkeypress(start_game, 'space')


score.menu()

screen.exitonclick()
