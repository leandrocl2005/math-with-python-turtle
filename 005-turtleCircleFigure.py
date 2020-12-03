import turtle
import tkinter as TK

screen = turtle.getscreen()
ted = turtle.Turtle()

screen.bgcolor("red")

ted.speed(9)
ted.shapesize(1, 1, 1)
ted.pensize(3)
ted.pencolor("white")
ted.fillcolor("red")
ted.shape("turtle")


for _ in range(24):
    ted.circle(100)
    ted.right(15)


TK.mainloop()