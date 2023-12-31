from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(40)
def move_backward():
    tim.backward(40)
def turn_left():
    tim.left(15)
def turn_right():
    tim.right(15)
def clear_screen():
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()