import turtle as t
import random

tim = t.Turtle()
tim.shape('classic')
t.colormode(255)

colors_list = [(236, 35, 108), (146, 28, 66), (239, 75, 35), (7, 148, 94), (220, 171, 45), 
                (182, 159, 48), (44, 191, 232), (28, 126, 194), (253, 223, 0), (125, 192, 79),
                (84, 28, 91), (245, 219, 50), (179, 40, 98), (42, 169, 116), (209, 131, 165), 
                (205, 56, 35), (239, 161, 192), (148, 25, 24), (242, 168, 156), (162, 211, 178),
                (26, 187, 225), (138, 210, 232), (7, 114, 55), (76, 135, 183), (112, 10, 8), (176, 190, 221)]

tim.penup()
x = -250
y = -250
tim.setpos(x, y)

for i in range(1, 11):
    tim.penup()
    tim.setpos(x, y + (50 * i))
    for j in range(10):
        r = random.choice(colors_list)[0]
        g = random.choice(colors_list)[1]
        b = random.choice(colors_list)[2]
        color_tup = (r, g, b)
        tim.pencolor(color_tup)
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()

screen = t.Screen()
screen.exitonclick()