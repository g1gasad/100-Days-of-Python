from turtle import Turtle, Screen
import random
import time

STARTING_POSITION = [(-40,0), (-20,0), (0,0)]
MOVE_DISTANCE = 20

UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[-1]
    def create_snake(self):
        for posi in STARTING_POSITION:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.speed('normal')
            new_segment.penup()
            new_segment.goto(posi)
            self.segments.append(new_segment)
    
    def move(self):
        for seg_num in range(len(self.segments) - 1):
            new_x = self.segments[seg_num+1].xcor()
            new_y = self.segments[seg_num+1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self): 
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    