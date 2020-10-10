def circle(j):
    for i in range(100):
        turtle.left(180-180*(98/100))
        turtle.forward(j)

def halfcircle(j):
    for i in range(50):
        turtle.right(180-180*(98/100))
        turtle.forward(j)

import numpy as np
import turtle

turtle.left(90)
turtle.color('yellow')
turtle.begin_fill()
circle(5)
turtle.end_fill()
turtle.penup()
turtle.forward(125/np.pi)
turtle.left(90)
turtle.forward(125/np.pi)
turtle.pendown()
turtle.color('black')
turtle.begin_fill()
circle(0.5)
turtle.end_fill()
turtle.penup()
turtle.forward(125/np.pi)
turtle.forward(125/np.pi)
turtle.pendown()
turtle.begin_fill()
circle(0.5)
turtle.end_fill()
turtle.penup()
turtle.left(180)
turtle.forward(125/np.pi)
turtle.right(90)
turtle.pendown()
turtle.width(2)
turtle.forward(125/np.pi)
turtle.penup()
turtle.left(90)
turtle.forward(125/np.pi)
turtle.right(90)
turtle.pendown()
turtle.color('red')
turtle.width(3)
halfcircle(2.5)
