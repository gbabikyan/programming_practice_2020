import turtle

turtle.shape('turtle')
turtle.forward(5)
for i in range(11):
    if i==0:
        continue
    turtle.forward(i*10/2)
    turtle.left(90)
    turtle.forward(i*10)
    turtle.left(90)
    turtle.forward(i*10)
    turtle.left(90)
    turtle.forward(i*10)
    turtle.left(90)
    turtle.forward(i*10/2)
    turtle.penup()
    turtle.right(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.pendown()