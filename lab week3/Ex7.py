import turtle

turtle.shape('turtle')
for i in range(1000):
    if i == 0:
        continue
    turtle.forward(1)
    turtle.left(180-180*((i-2)/i))