#####Turtle Intro######

from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("red")

######## Challenge 1 - Draw a Square ############

def square():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    
square()

screen = Screen()
screen.exitonclick()

