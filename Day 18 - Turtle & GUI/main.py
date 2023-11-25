from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
tim.color('sienna')

def dashed_line(length):
    for _ in range(length):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

for d in range(4):
    dashed_line(15)
    tim.left(90)


screen = Screen()
screen.exitonclick()