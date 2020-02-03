#!/usr/bin/python3

#This module is a basic code for a Classic ping pong game

import turtle
#import the turtle library to create all graphical instructions

#Basic window configuration
w = turtle.Screen()
w.title("Super Ping Pong Game     @karlgarmor")
w.bgcolor("black")
w.setup(width = 800, height = 600)
w.tracer(0)



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





#infinite loop to excecute all instruction in the game
while True:
    w.update() 


