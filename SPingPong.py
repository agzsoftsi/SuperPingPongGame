#!/usr/bin/python3

#This module is a basic code for a Classic ping pong game

import turtle
#import the turtle library to create all graphical instructions

#Basic window configuration
w = turtle.Screen()
w.title("Super Ping Pong Game     @karlgarmor")
w.bgcolor("black")
w.setup(width = 800, height = 600)
#w.tracer(8, 25)




#Players Configuration
#player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("red")
player1.penup()
player1.goto(-350, 0)
player1.shapesize(stretch_wid = 5, stretch_len = 1)

#player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("blue")
player2.penup()
player2.goto(350, 0)
player2.shapesize(stretch_wid = 5, stretch_len = 1)


#create ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.x = 2
ball.y = 2

#functions to move each one players
#functions player1 to up
def player1_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)

#functions player1 to down
def player1_down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)

#functions player2 to up
def player2_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)


#functions player1 to down
def player2_down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)



#configure keyboard to listen the functions
w.listen()
w.onkeypress(player1_up, "w")
w.onkeypress(player1_down, "s")
w.onkeypress(player2_up, "Up")
w.onkeypress(player2_down, "Down")




#infinite loop to excecute all instruction in the game
while True:
    w.update()

    #configure move of ball
    ball.setx(ball.xcor() + ball.x)
    ball.sety(ball.ycor() + ball.y)

    #configure ball in border
    if ball.ycor() > 290:
        ball.y *= -1

    if ball.ycor() < -290:
        ball.y *= -1

    #configure ball in final score
    if ball.xcor() > 390:
        ball.goto(0,0)

    if ball.xcor() < -390:
        ball.goto(0,0)

    #configure ball collision with players
    if ((ball.xcor() < -340 and ball.xcor() > -350)
           and (ball.ycor() < player1.ycor() + 50
           and ball.ycor() > player1.ycor() - 50)):
        ball.x *= -1

    if ((ball.xcor() > 340 and ball.xcor() < 350)
           and (ball.ycor() < player2.ycor() + 50
           and ball.ycor() > player2.ycor() - 50)):
        ball.x *= -1



