from turtle import Turtle, Screen
from seaborn import color_palette
import random

color_pal = color_palette()
tim = Turtle()
tim.shape('turtle')

def draw_shape(num_sides):
    tim.color(random.choice(color_pal))
    s = (num_sides - 2) * 180
    angle = s // num_sides
    for n in range(num_sides):
        tim.forward(100)
        tim.left(180 - angle)

for i in range(3, 10):
    draw_shape(i)






screen = Screen()
screen.exitonclick()