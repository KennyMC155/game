from functions import *


while True:
    create_game_win()
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
        ball_return()
        score_a += 1
        pen.clear()
        pen.write(f"{player_a}: {score_a} || {player_b}: {score_b}", align="center", font=("Verdana", 22, "normal"))

    if ball.xcor() < -390:
        ball_return()
        score_b += 1
        pen.clear()
        pen.write(f"{player_a}: {score_a} || {player_b}: {score_b}", align="center", font=("Verdana", 22, "normal"))

    rocket_push()
    get_win(score_a, score_b)
