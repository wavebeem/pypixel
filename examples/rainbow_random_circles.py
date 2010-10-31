#!/usr/bin/python2

from pypixel import *

show()

h = 0
while True:
    x  = random(WIDTH)
    y  = random(HEIGHT)
    r  = random(50, 100)
    h += 1
    h %= 360
    s  = 100
    v  = 100
    c  = hsv2rgb((h, s, v))
    circle(c, (x, y), r)
    update()
