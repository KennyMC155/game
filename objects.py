import turtle

win = turtle.Screen()
win.title("Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# rockets
rocket_left = turtle.Turtle()
rocket_left.speed(0)
rocket_left.shape("square")
rocket_left.color("green")
rocket_left.shapesize(stretch_len=1, stretch_wid=5)
rocket_left.penup()
rocket_left.goto(-350, 0)

rocket_right = turtle.Turtle()
rocket_right.speed(0)
rocket_right.shape("square")
rocket_right.color("red")
rocket_right.shapesize(stretch_len=1, stretch_wid=5)
rocket_right.penup()
rocket_right.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("turtle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: 0 || Player B: 0", align="center", font=("Verdana", 22, "normal"))
