import turtle as t
from seaborn import color_palette
import random

t.colormode(255)
color_pal = color_palette()
tim = t.Turtle()
tim.shape('turtle')
tim.pensize(9)
tim.speed('fastest')
angle_list = [0, 90, 180, 270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)


for i in range(100):
    angle = random.choice(angle_list)
    color = random.choice(color_pal)
    rgb_color_tuple = random_color()
    tim.pencolor(rgb_color_tuple)
    tim.setheading(angle)
    tim.forward(30)




screen = t.Screen()
screen.exitonclick()