def circle1(i:int):

    for j in range(50):
        turtle.right(180-180*(98/100))
        turtle.forward(i)
def circle2(i:int):

    for j in range(50):
        turtle.right(180-180*(98/100))
        turtle.forward(i/10)

import turtle

turtle.shape('turtle')
turtle.left(90)
for i in range(6):
    circle1(5)
    circle2(5)
