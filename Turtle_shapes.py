#Drawing shapes

from turtle import *

t = Turtle()
t.shape("turtle")
screen = Screen()
side_length = int(input("What would you like your side length to be ? "))
#shape 1 triangle
def draw_triangle(side_length):
    for _ in range(2):
        t.forward(side_length)
        t.left(60)
    t.home()

draw_triangle(side_length)

t.clear()

#shape 2 square

def draw_square(side_length):
     for _ in range(4):
         t.forward(side_length)
         t.left(90)

draw_square(side_length)

t.clear()
#shape 3 pentagon

def draw_pentagon(side_length):
   for _ in range(5):
       t.forward(side_length)
       t.left(72)

draw_pentagon(side_length)

t.clear()




screen.exitonclick()
   
