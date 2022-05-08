import time
from turtle import *

pen = Turtle()
pen.color('red')
bgcolor('#e6e6e6')


def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)


def draw_heart():
    pen.pensize(5)
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
    time.sleep(15)


draw_heart()
