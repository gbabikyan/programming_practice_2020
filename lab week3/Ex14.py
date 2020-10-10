def star(i):
    for j in range(i):
        turtle.forward(100)
        turtle.right(180 - 180/i)

import turtle

turtle.shape('turtle')
star(5)
turtle.penup()
turtle.forward(200)
turtle.pendown()
star(11)