# Simple Pong game
# By Sergei Demianenko(@HarmaH) 28.01.2020

import turtle
import os

wind = turtle.Screen()
wind.title("Pong by @HarmaH")
wind.bgcolor('black')
wind.setup(width = 800, height = 600)
wind.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(5)
paddleA.shape('square')
paddleA.color('white')
paddleA.shapesize(stretch_wid = 5, stretch_len = 1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(5)
paddleB.shape('square')
paddleB.color('white')
paddleB.shapesize(stretch_wid = 5, stretch_len = 1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(5)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align = 'center', font = ("Courier", 24, "normal"))

# Functions
def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

# Keyboard binding   
wind.listen()
wind.onkeypress(paddleA_up, 'w')
wind.onkeypress(paddleA_down, 's')
wind.onkeypress(paddleB_up, 'Up')
wind.onkeypress(paddleB_down, 'Down')

# Main game loop
while True:
    wind.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay /Users/serhiidemianenko/Desktop/py.self/PongGame/320549__debsound__pop-19.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay /Users/serhiidemianenko/Desktop/py.self/PongGame/320549__debsound__pop-19.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(scoreA, scoreB), align = 'center', font = ("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(scoreA, scoreB), align = 'center', font = ("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay /Users/serhiidemianenko/Desktop/py.self/PongGame/320549__debsound__pop-19.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay /Users/serhiidemianenko/Desktop/py.self/PongGame/320549__debsound__pop-19.wav&")
        