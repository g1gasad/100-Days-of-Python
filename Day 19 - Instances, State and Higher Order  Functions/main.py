from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color:')
colors = ['red', 'orange', 'green', 'blue', 'yellow', 'purple']
y_positions = [-130, -80, -30, 20, 70, 120]
all_turtles = []

for turtle_index in range(6):
    turt = Turtle(shape='turtle')
    turt.color(colors[turtle_index])
    turt.penup()
    turt.goto(x=-280, y=y_positions[turtle_index])
    all_turtles.append(turt)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 0:
            is_race_on = False
            winner_color = turtle.pencolor().title()
            if winner_color.lower() == user_bet.lower():
                print(f"You've won, The {winner_color} turtle is the winner")
            else:
                print(f"You've lost, The {winner_color} turtle is the winner")

screen.exitonclick()
