import turtle

screen = turtle.getscreen()
ted = turtle.Turtle()

screen.bgcolor("red")

ted.speed(1)
ted.shapesize(2, 2, 2)
ted.pensize(5)
ted.pencolor("white")
ted.fillcolor("red")
ted.shape("turtle")

ted.begin_fill()

ted.forward(100)
for _ in range(3):
    ted.right(90)
    ted.forward(100)

ted.end_fill()