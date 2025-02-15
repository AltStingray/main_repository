import turtle as t
from turtle import Screen
import random

random_walk = t.Turtle()
random_walk.shapesize(0.1, 0.1)
random_walk.pensize(10)
random_walk.speed(0)
random_walk.ondrag(fun=1, btn=1)

def random_color():
    t.colormode(255)
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for walk in range(99999):
    directions = [0, 90, 180, 270]
    random_walk.color(random_color())
    random_walk.forward(25)
    random_walk.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()