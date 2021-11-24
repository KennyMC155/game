from functions import *

ball = create_ball()
left_rocket = creeate_roket("blue", -350)
right_rocket = creeate_roket("red", 350)
pen = create_score_board()

while True:
    create_game_win(left_rocket, right_rocket)
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
        ball_return(ball)
        score_a += 1
        pen.clear()
        pen.write(f"{player_a}: {score_a} || {player_b}: {score_b}", align="center", font=("Verdana", 22, "normal"))

    if ball.xcor() < -390:
        ball_return(ball)
        score_b += 1
        pen.clear()
        pen.write(f"{player_a}: {score_a} || {player_b}: {score_b}", align="center", font=("Verdana", 22, "normal"))

    rocket_push(ball, left_rocket, right_rocket)
    get_win(pen, score_a, score_b, ball, left_rocket, right_rocket)
