from turtle import *
import random

t = Turtle()
screen = Screen()
t.shape("turtle")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    Color = (r, g, b)
    return Color
NEWS = [ 0, 90, 180, 270 ]

def random_walk():
    t.pensize(15)
    t.speed("fastest")
    t.forward(100)
    t.setheading((random.choice(NEWS)))

for shapeside in range (0,100):
    t.color(random_color())
    random_walk()

screen.exitonclick()






































































