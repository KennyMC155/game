import turtle
import random

score = 2
score_a = 0
score_b = 0
Player_a = "Left Player"
Player_b = "Right Player"


def create_game_win(left_rocket, right_rocket):
    win = turtle.Screen()
    win.title("Game")
    win.bgcolor("black")
    win.setup(width=800, height=600)
    win.tracer(0)
    win.listen()
    win.onkeypress(lambda: rocket_up(left_rocket), "w")
    win.onkeypress(lambda: rocket_down(left_rocket), "s")
    win.onkeypress(lambda: rocket_up(right_rocket), "Up")
    win.onkeypress(lambda: rocket_down(right_rocket), "Down")
    win.update()
    return win


def creeate_roket(color, postion_cord):
    rocket = turtle.Turtle()
    rocket.speed(0)
    rocket.shape("square")
    rocket.color(color)
    rocket.shapesize(stretch_len=1, stretch_wid=5)
    rocket.penup()
    rocket.goto(postion_cord, 0)
    return rocket


# create ball
def create_ball():
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("turtle")
    ball.color("yellow")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = random.randint(2, 10)
    ball.dy = random.randint(2, 10)
    return ball


# create_score_board
def create_score_board():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write(f"{Player_a}: {score_a} || {Player_b}: {score_b}", align="center", font=("Verdana", 22, "normal"))
    return pen


# rockets movement
def rocket_up(rocket):
    y = rocket.ycor()
    if y < 250:
        y += 20
        rocket.sety(y)


def rocket_down(rocket):
    y = rocket.ycor()
    if y > -250:
        y -= 20
        rocket.sety(y)


def clean_win(pen, ball, left_rocket, right_rocket):
    pen.clear()
    ball.clear()
    left_rocket.clear()
    right_rocket.clear()


# ball return
def ball_return(ball):
    ball.goto(0, 0)
    ball.dy = random.randint(7, 15)
    ball.dx *= -1


def get_win(pen, score_a, score_b):
    if score_a > score:
        pen.write(f"{Player_a} Win", align="center", font=("Verdana", 22, "normal"))
    elif score_b > score:
        pen.write(f"{Player_b} Win", align="center", font=("Verdana", 22, "normal"))
    else:
        pass


# ball movement
def rocket_push(ball, left_rocket, right_rocket):
    if ball.xcor() > 340 and right_rocket.ycor() + 50 > ball.ycor() > right_rocket.ycor() - 50:
        ball.dx *= -1
    if ball.xcor() < -340 and left_rocket.ycor() + 50 > ball.ycor() > left_rocket.ycor() - 50:
        ball.dx *= -1
