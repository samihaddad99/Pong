# Filename: Pong.py
# Author: Sami Haddad
# Date Created: 3/9/2022
# Last Modified: 3/9/2022
# Source(s): https://www.youtube.com/watch?v=C6jJg9Zan7w&ab_channel=freeCodeCamp.org
# Pong.py recreates the classic Pong game 
#   using Python with the turtle library
#   and the winsound library to generate the sounds

import turtle
import winsound


wn = turtle.Screen() #create an instance of Screen from the turtle class
wn.title("Pong by Sami")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #speed up the game

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() # a turtle object
paddle_a.speed(0) # speed of animation - maximum
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #size is 20px*20px by default
paddle_a.penup() #turtles draw a line by default, so this disables that
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle() # a turtle object
paddle_b.speed(0) # speed of animation - maximum
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #size is 20px*20px by default
paddle_b.penup() #turtles draw a line by default, so this disables that
paddle_b.goto(+350, 0)

# Ball
ball = turtle.Turtle() # a turtle object
ball.speed(0) # speed of animation - maximum
ball.shape("square")
ball.color("white")
ball.penup() #turtles draw a line by default, so this disables that
ball.goto(0, 0)
ball.dx = 0.1 # calling it dx (delta/change in x)
ball.dy = -0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor() #gety
    y += 20
    paddle_a.sety(y) #sety

def paddle_a_down():
    y = paddle_a.ycor() #gety
    y -= 20
    paddle_a.sety(y) #sety

def paddle_b_up():
    y = paddle_b.ycor() #gety
    y += 20
    paddle_b.sety(y) #sety

def paddle_b_down():
    y = paddle_b.ycor() #gety
    y -= 20
    paddle_b.sety(y) #sety

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop (every game needs this)
while True:

    wn.update() #everytime loop runs it will up

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        


