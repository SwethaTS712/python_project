from turtle import *
import random
tinny =Turtle()
tinny.speed(2)
tinny.pensize(3)
tinny.shape("turtle")
color = ['cyan2','coral3','red','Limegreen','Violet','chocolate2']

def circle():
    radius=100
    for i in range(4):
        tinny.color(random.choice(color))
        tinny.penup()
        tinny.goto(0,0)
        tinny.pendown()
        tinny.circle(radius)
        radius-=25

circle()
screen=Screen()
screen.exitonclick()