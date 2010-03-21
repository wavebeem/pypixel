#!/usr/bin/python

from pypixel import *

title("Polar graphing demo")
show()

def f(theta):
    K = 4
    return -HEIGHT/2.5 * sin(K * theta)

theta  = 0
radius = 48

STEP_SIZE = 500

while True:
    for i in xrange(STEP_SIZE):
        hue   = int(theta/10.0)
        color = hsv((hue, 100, 100))

        r = f(theta)
        point = polar((r, theta))

        circle(color, point, radius)

        theta += 0.1
        theta %= 360 * 10.0

    update()
    # clear()
