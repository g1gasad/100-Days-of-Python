from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

starting_position = [(-40,0), (-20,0), (0,0)]
segments = []

for posi in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(posi)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for seg_num in range(3):
        segments[seg_num].forward(10)
        



screen.exitonclick()


32*2.5