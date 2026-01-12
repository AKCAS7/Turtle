from turtle import *
import random

t = Turtle()
screen = Screen()
t.shape("turtle")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
NEWS = [ 0, 90, 180, 270 ]

def random_walk():
    t.forward(100)
    t.right(random.choice(NEWS))

for shapeside in range (0,100):
    t.color(random.choice(colours))
    random_walk()

screen.exitonclick()





































































