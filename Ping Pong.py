# Ping Pong Python Game

# Left Paddle - use W and S keys on keyboard
# Right Paddle - use UP and DOWN arrow keys on keyboard


# turtle graphics standard library
import turtle
import winsound

# Window screen
win = turtle.Screen()
win.title("Ping Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("yellow")
pad_a.shapesize(stretch_wid=6, stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)

# Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("orange")
pad_b.shapesize(stretch_wid=6, stretch_len=1)
pad_b.penup()
pad_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("purple")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.116     # change speed of ball values
ball.dy = -0.116    # change speed of ball values

# Pen Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def pad_a_up():
	y = pad_a.ycor()
	y += 20
	pad_a.sety(y)

def pad_a_down():
	y = pad_a.ycor()
	y -= 20
	pad_a.sety(y)

def pad_b_up():
	y = pad_b.ycor()
	y += 20
	pad_b.sety(y)

def pad_b_down():
	y = pad_b.ycor()
	y -= 20
	pad_b.sety(y)

# Keyboard binding
win.listen()
win.onkeypress(pad_a_up, "w")
win.onkeypress(pad_a_down, "s")
win.onkeypress(pad_b_up, "Up")
win.onkeypress(pad_b_down, "Down")

# Main game loop
while True:
    win.update()

	# Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

	# Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("Ping Pong Border Collision.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("Ping Pong Border Collision.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions (including sounds)
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("Metal Ping Pong.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("Metal Ping Pong.wav", winsound.SND_ASYNC)
