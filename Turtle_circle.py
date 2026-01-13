from turtle import *

t = Turtle()

def circle():
    t.shape("turtle")
    t.pensize("1")
    t.speed("fastest")
    t.circle(100)
    for _ in range(36):
        current_heading = t.heading()
        t.setheading(current_heading + 10 )
        t.circle(100)

circle()

screen = Screen()
screen.exitonclick()
