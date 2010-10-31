#!/usr/bin/python2

from pypixel import *

show()

x,     y = 0, HEIGHT
v_x, v_y = 5, -20
a_x, a_y = 0, 0.4

while not (y > HEIGHT):
    x += v_x
    y += v_y

    v_x += a_x
    v_y += a_y

    int_x = int(x)
    int_y = int(y)

    line(RED, (0, HEIGHT), (int_x, int_y), 10)
    circle(RED, (int_x, int_y), 20)

    update()

    line(BLACK, (0, HEIGHT), (int_x, int_y), 10)
    circle(BLACK, (int_x, int_y), 20)
