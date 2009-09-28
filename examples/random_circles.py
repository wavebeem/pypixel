#!/usr/bin/python

from pypixel import *

show()

while True:
    x = random(WIDTH)
    y = random(HEIGHT)
    r = random(1, 100)
    h = random(360)
    s = 100
    v = 100
    c = hsv((h, s, v))
    circle(c, (x, y), r)
    update()
