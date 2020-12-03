import turtle
import tkinter as TK
import numpy as np
import math


screen = turtle.getscreen()
ted = turtle.Turtle()

screen.bgcolor("red")

ted.speed(9)
ted.shapesize(1, 1, 1)
ted.pensize(3)
ted.pencolor("white")
ted.fillcolor("blue")
ted.shape("turtle")

# paramétricas da parábola
# def parametric_x(t):
#    return t
# def parametric_y(t):
#    return int(-200 + 0.005 * t ** 2)
# t_start = -301
# t_end = 301
# precision = 2

# paramétricas do circulo
# def parametric_x(t):
#    return int(100 * np.cos(2 * np.pi / 600 * t))
# def parametric_y(t):
#    return int(100 * np.sin(2 * np.pi / 600 * t))
# t_start = -301
# t_end = 301
# precision = 2

# paramétricas do circulo
# def parametric_x(t):
#    return int(t * np.cos(2 * np.pi / 75 * t))
# def parametric_y(t):
#    return int(t * np.sin(2 * np.pi / 75 * t)) + 20
# t_start = 0
# t_end = 301
# precision = 2


def theta(t):
    return 2 * np.pi / 1201 * t


def r(t):
    return np.cos(8 * theta(t))


def parametric_x(t):
    return int(250 * r(t) * np.cos(theta(t)))


def parametric_y(t):
    return int(250 * r(t) * np.sin(theta(t)))


t_start = 0
t_end = 1201
precision = 1


steps = np.arange(t_start, t_end, precision)
ted.penup()
ted.goto(parametric_x(t_start), parametric_y(t_start))  # start point
ted.pendown()

ted.begin_fill()
for i in range(len(steps)):
    if i != 0:
        diff_xt = (parametric_x(steps[i]) - parametric_x(steps[i - 1])) / precision
        diff_yt = (parametric_y(steps[i]) - parametric_y(steps[i - 1])) / precision
        cos_angle = diff_xt / math.sqrt(diff_xt ** 2 + diff_yt ** 2 + 0.0001)
        angle = math.acos(cos_angle)
        if diff_yt < 0:
            angle = -angle
        ted.setheading(math.degrees(angle))
    ted.goto(parametric_x(steps[i]), parametric_y(steps[i]))
ted.end_fill()

TK.mainloop()
