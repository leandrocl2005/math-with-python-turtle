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


steps = np.arange(-300, 301, 1)
ted.penup()
ted.goto(-300, 250)
ted.pendown()

for i in steps:
    ted.setheading(math.degrees(math.atan(0.01 * i)))
    ted.goto(i, -200 + math.floor(0.005 * i * i))


TK.mainloop()
