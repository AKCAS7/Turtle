from turtle import Turtle, Screen

t=Turtle()

t.shape("turtle")

def dashed_line():
    for I in range(10):
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)

dashed_line()

screen = Screen()
screen.exitonclick()
