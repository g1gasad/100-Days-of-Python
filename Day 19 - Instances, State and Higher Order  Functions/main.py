from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color:')

tim = Turtle(shape='turtle')
tim.penup()
tim.goto(x=-280, y=0)

screen.exitonclick()
