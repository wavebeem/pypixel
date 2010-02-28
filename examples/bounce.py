#!/usr/bin/python

from pypixel import *

import sys

show()

w, h = 200, 200
x, y = WIDTH/2, 0

v_y = 0.1
a_y = 1
while not (v_y == 0):
    ix = int(x)
    iy = int(y)
    ellipse(RED, ((ix, iy), (w, h)), center=True)
    update()
    ellipse(BLACK, ((ix, iy), (w, h)), center=True)
    y   += v_y
    v_y += a_y
    if y > HEIGHT:
        v_y *= -0.9
    if abs(v_y) < 0.05 and (HEIGHT - h) < y < HEIGHT:
        v_y = 0
