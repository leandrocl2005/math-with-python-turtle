import turtle
import tkinter as TK
import numpy as np
import math


screen = turtle.getscreen()
ted = turtle.Turtle()

screen.bgcolor("red")

ted.speed(100)
ted.shapesize(1, 1, 1)
ted.pensize(3)
ted.pencolor("white")
ted.fillcolor("red")
ted.shape("turtle")

x_start = -300
x_end = 301
precision = 2

# parabola
# def f(x):
#    return int(-200 + 0.005 * x ** 2)


# cosine
def f(x):
    return int(200 * np.cos(0.05 * x))


steps = np.arange(x_start, x_end, precision)
ted.penup()
ted.goto(x_start, f(x_start))  # start point
ted.pendown()

for i in range(len(steps)):
    if i != 0:
        ted.setheading(
            math.degrees(
                math.atan(f(steps[i]) / precision - f(steps[i - 1]) / precision)
            )
        )
    ted.goto(steps[i], f(steps[i]))


TK.mainloop()
