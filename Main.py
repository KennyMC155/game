import functions

ball = functions.create_ball()
left_rocket = functions.creeate_roket("blue", -350)
right_rocket = functions.creeate_roket("red", 350)
pen = functions.create_score_board()

while True:
    functions.create_game_win(left_rocket, right_rocket)
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
        functions.ball_return(ball)
        functions.score_a += 1
        pen.clear()
        pen.write(f"{functions.player_a}: {functions.score_a} || {functions.player_b}: {functions.score_b}", align="center", font=("Verdana", 22, "normal"))

    if ball.xcor() < -390:
        functions.ball_return(ball)
        functions.score_b += 1
        pen.clear()
        pen.write(f"{functions.player_a}: {functions.score_a} || {functions.player_b}: {functions.score_b}", align="center", font=("Verdana", 22, "normal"))

    functions.rocket_push(ball, left_rocket, right_rocket)
    functions.get_win(pen, functions.score_a, functions.score_b, ball, left_rocket, right_rocket)
