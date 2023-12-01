from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")

starting_position = [(-40,0), (-20,0), (0,0)]
segments = []

for posi in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.goto(posi)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(5)
        # if seg.ycor() == 100:

        if seg.pos() == (200, 0):
            seg.left(90)
        if seg.pos() == (200, 200):
            seg.left(90)
        if seg.pos() == (-200, 200):
            seg.left(90)
        if seg.pos() == (-200, -200):
            seg.left(90)




# snake_body()

def take_a_left(turt):
    if turt.xcor() == 200:
        turt.left(90)








screen.exitonclick()