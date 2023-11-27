import turtle as t
from seaborn import color_palette
import random

t.colormode(255)
color_pal = color_palette()
tim = t.Turtle()
tim.shape('classic')
tim.pensize(2)
tim.speed('fastest')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

def draw_spirograph(tilt):
    for i in range(0, 360, tilt):
        rgb_color_tuple = random_color()
        tim.pencolor(rgb_color_tuple)
        tim.setheading(i)
        tim.circle(120)

draw_spirograph(2)

screen = t.Screen()
screen.exitonclick()