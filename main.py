import turtle
import random

dots = turtle.Turtle()
dots.speed("fast")
dots.hideturtle()
screen = turtle.Screen()
screen.colormode(255)
screen.screensize(500, 500)

colors = [(230, 207, 91), (225, 149, 91), (122, 167, 187), (35, 110, 158), (163, 13, 22), (127, 177, 145),
          (233, 81, 49), (202, 67, 27), (192, 186, 23), (174, 18, 13), (33, 129, 49), (7, 99, 37), (13, 64, 39),
          (12, 41, 76), (242, 203, 4), (139, 79, 92), (88, 13, 20), (53, 166, 76), (51, 23, 19), (180, 134, 146),
          (6, 64, 137), (213, 68, 75), (230, 170, 161), (49, 151, 191), (77, 133, 186), (175, 204, 176)]

starting_y = -250

while starting_y != 250:
    dots.penup()
    dots.goto(-250, starting_y)
    for _ in range(10):
        dots.dot(20, random.choice(colors))
        dots.forward(50)
    starting_y += 50

screen.exitonclick()
