import turtle
import tkinter as TK

screen = turtle.getscreen()
ted = turtle.Turtle()

screen.bgcolor("#38363F")

ted.speed(6)
ted.shapesize(2, 2, 2)
ted.pensize(3)
ted.pencolor("#F4F1F0")
ted.fillcolor("#83795B")
ted.shape("turtle")


def drawSquare(ted):
    ted.forward(100)
    for _ in range(3):
        ted.right(90)
        ted.forward(100)


ted.begin_fill()

for _ in range(24):
    drawSquare(ted)
    ted.right(15)

ted.end_fill()

TK.mainloop()