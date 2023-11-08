from turtle import Turtle, Screen
from seaborn import color_palette
import random

color_pal = color_palette()
color_pal[0]

timmy = Turtle()
johny = Turtle()
# print(timmy)
johny.shape("turtle")
timmy.shape("turtle")
timmy.color('red', 'aquamarine')

for move in range(10, 501, 10):
    color_int = random.randint(0,9)
    timmy.color(color_pal[color_int])
    timmy.forward(move)
    timmy.left(angle=90)
    johny.color(color_pal[-color_int])
    johny.forward(move+10)
    johny.right(angle=90)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()