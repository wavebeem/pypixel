#!/usr/bin/python2

from pypixel import *

show()

while True:
    x = random(WIDTH)
    y = random(HEIGHT)
    radius = random(1, 100)
    h = random(360, end=False)
    s = 100
    v = 100
    hsv = (h, s, v)
    color = hsv2rgb(hsv)
    point = (x, y)
    circle(color, point, radius)
    update()
