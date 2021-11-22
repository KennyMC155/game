import time
import turtle

score = 1
score_a = 0
score_b = 0
player_a = "Left Player"
player_b = "Right Player"


def create_game_win():
    win = turtle.Screen()
    win.title("Game")
    win.bgcolor("black")
    win.setup(width=800, height=600)
    win.tracer(0)
    win.listen()
    win.onkeypress(rocket_left_up, "w")
    win.onkeypress(rocket_left_down, "s")
    win.onkeypress(rocket_right_up, "Up")
    win.onkeypress(rocket_right_down, "Down")
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


left_rocket = creeate_roket("blue", -350)
right_rocket = creeate_roket("red", 350)


# create ball
def create_ball():
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("turtle")
    ball.color("yellow")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 4
    ball.dy = 4
    return ball


ball = create_ball()


# create_score_board
def create_score_board():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write(f"{player_a}: {score_a} || {player_b}: {score_b}", align="center", font=("Verdana", 22, "normal"))
    return pen


pen = create_score_board()


# rockets movement


def rocket_left_up():
    y = left_rocket.ycor()
    if y < 250:
        y += 20
        left_rocket.sety(y)


def rocket_left_down():
    y = left_rocket.ycor()
    if y > -250:
        y -= 20
        left_rocket.sety(y)


def rocket_right_up():
    x = right_rocket.ycor()
    if x < 250:
        x += 20
        right_rocket.sety(x)


def rocket_right_down():
    x = right_rocket.ycor()
    if x > - 250:
        x -= 20
        right_rocket.sety(x)


# ball movement

def clean_win():
    pen.clear()
    ball.clear()
    left_rocket.clear()
    right_rocket.clear()


# ball return
def ball_return():
    ball.goto(0, 0)
    ball.dx *= -1


def get_win(score_a, score_b):
    if score_a > score:
        clean_win()
        pen.write(f"{player_a} Win", align="center", font=("Verdana", 22, "normal"))
        time.sleep(3)
        turtle.bye()
    elif score_b > score:
        clean_win()
        pen.write(f"{player_b} Win", align="center", font=("Verdana", 22, "normal"))
        time.sleep(3)
        turtle.bye()


def rocket_push():
    if ball.xcor() > 340 and ball.ycor() < right_rocket.ycor() + 50 and ball.ycor() > right_rocket.ycor() - 50:
        ball.dx *= -1
    if ball.xcor() < -340 and ball.ycor() < left_rocket.ycor() + 50 and ball.ycor() > left_rocket.ycor() - 50:
        ball.dx *= -1
