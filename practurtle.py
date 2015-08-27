__author__ = 'user'

import turtle
def drawSquare(length):
    for i in range(101):
        for j in range(2):
            turtle.forward(length+i*2)
            turtle.right(90+j)

turtle.color("green")
drawSquare(100)
