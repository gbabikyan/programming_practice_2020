import turtle

turtle.shape('turtle')
turtle.forward(5)
for i in range(20):
    if i==0:
        continue
    turtle.forward(i*10)
    turtle.left(90)