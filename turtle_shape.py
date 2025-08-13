from turtle import *
import random
tinny = Turtle()
tinny.pensize(3)
colours=["red","blue","green","pink","torquish",'cyan2','coral3','Limegreen','Violet','chocolate2']

def draw(num_sides):
    angle=360/num_sides
    for i in range(num_sides):
        tinny.forward(100)
        tinny.right(angle)

for side in range(3,11):
    tinny.color(random.choice(colours))
    draw(side)

screen = Screen()
screen.exitonclick()

