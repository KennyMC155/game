import time
from objects import *


# score_a = 0
# score_b = 0

# rockets movement

def rocket_left_up():
    y = rocket_left.ycor()
    if y < 250:
        y += 20
        rocket_left.sety(y)


def rocket_left_down():
    y = rocket_left.ycor()
    if y > -250:
        y -= 20
        rocket_left.sety(y)


def rocket_right_up():
    x = rocket_right.ycor()
    if x < 250:
        x += 20
        rocket_right.sety(x)


def rocket_right_down():
    x = rocket_right.ycor()
    if x > - 250:
        x -= 20
        rocket_right.sety(x)


# ball movement

def win_side(score_a, score_b):
    if score_a > 1:
        pen.clear()
        ball.clear()
        rocket_left.clear()
        rocket_right.clear()
        pen.write("Player A Win", align="center", font=("Verdana", 22, "normal"))
        time.sleep(5)
        turtle.bye()
    elif score_b > 1:
        pen.clear()
        ball.clear()
        rocket_left.clear()
        rocket_right.clear()
        pen.write("Player B Win", align="center", font=("Verdana", 22, "normal"))
        time.sleep(5)
        turtle.bye()


def rocket_push():
    if ball.xcor() > 340 and ball.ycor() < rocket_right.ycor() + 50 and ball.ycor() > rocket_right.ycor() - 50:
        ball.dx *= -1
    if ball.xcor() < -340 and ball.ycor() < rocket_left.ycor() + 50 and ball.ycor() > rocket_left.ycor() - 50:
        ball.dx *= -1
