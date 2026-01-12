#Drawing shapes

from turtle import *

t = Turtle()
t.shape("turtle")
screen = Screen()
side_length = int(input("What would you like your side length to be ? "))

def draw_polygon(t, sides, side_length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(side_length)
        t.left(angle)
    t.home()

# Triangle
draw_polygon(t, 3, side_length)
t.clear()

# Square
draw_polygon(t, 4, side_length)
t.clear()

# Pentagon
draw_polygon(t, 5, side_length)
t.clear()

screen.exitonclick()
   

