def circle1(i:int):

    for j in range(100):
        turtle.left(180-180*(98/100))
        turtle.forward(i)
def circle2(i:int):

    for j in range(100):
        turtle.right(180-180*(98/100))
        turtle.forward(i)

import turtle

turtle.shape('turtle')
turtle.left(90)
for i in range(6):
    circle1((i+1)*2)
    circle2((i+1)*2)
