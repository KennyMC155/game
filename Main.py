from functions import *

# keyboard
win.listen()
win.onkeypress(rocket_left_up, "w")
win.onkeypress(rocket_left_down, "s")
win.onkeypress(rocket_right_up, "Up")
win.onkeypress(rocket_right_down, "Down")

score_a = 0
score_b = 0

while True:
    win.update()
    # ball movements
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} || Player B: {score_b}", align="center", font=("Verdana", 22, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} || Player B: {score_b}", align="center", font=("Verdana", 22, "normal"))

    rocket_push()
    win_side(score_a, score_b)
