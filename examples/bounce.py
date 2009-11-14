#!/usr/bin/python

from pypixel import *
from math    import fabs

import sys

show()

w, h = 200, 200
x, y = WIDTH/2 - w/2, 0

v_y = 0.1
a_y = 1
while not (v_y == 0):
    ix = int(x)
    iy = int(y)
    ellipse(RED, ((ix, iy), (w, h)))
    update()
    ellipse(BLACK, ((ix, iy), (w, h)))
    y   += v_y
    v_y += a_y
    if y > HEIGHT:
        v_y *= -0.9
    if fabs(v_y) < 0.05 and (HEIGHT - h) < y < HEIGHT:
        v_y = 0
