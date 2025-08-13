from turtle import *
import random
tinny = Turtle()
directions=[0,90,180,270]
colours=['cyan2','coral3','red','Limegreen','Violet','chocolate2']
tinny.pensize(15)
tinny.speed('fastest')
for i in range(100):
    tinny.color(random.choice(colours))
    tinny.forward(30)
    tinny.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
