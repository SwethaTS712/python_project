from turtle import *
import random

tinny =Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
a=colormode(255)
tinny.speed('fastest')

def spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tinny.color(random_color())
        tinny.circle(100)
        current_heading = tinny.heading()
        tinny.setheading(current_heading + size_of_gap)

spirograph(5)
screen = Screen()
screen.exitonclick()