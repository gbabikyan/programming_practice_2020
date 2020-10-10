import turtle

turtle.shape('turtle')

for i in range(10):
    for j in range(i+3):
        if j == 0:
            a = 180 * (i+1) / (i+3) / 2
            a = 180 - a
        else:
            a = 180*(i+1) / (i+3)
            a = 180 - a
        if i == 0:
            b = 90
        else:
            b = 100
        turtle.left(a)
        turtle.forward(b)
    turtle.penup()
    turtle.right(180 * (i+1) / (i+3) / 2)
    turtle.forward(10)
    turtle.pendown()