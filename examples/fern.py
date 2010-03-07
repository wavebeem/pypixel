#!/usr/bin/python

from pypixel import *

title("Fern demo")
show()

x, y = 0, 0

step_size = 1000
scale = 45

while True:
    for i in xrange(step_size):
        chance = random(1, 100)
        if chance <= 1:
            xn = 0
            yn = 0.16 * y
        elif chance <= (1 + 7):
            xn = 0.20 * x - 0.26 * y
            yn = 0.23 * x + 0.22 * y + 1.6
        elif chance <= (1 + 7 + 7):
            xn = 0.15 * x + 0.28 * y
            yn = 0.26 * x + 0.24 * y + 0.44
        else:
            xn =  0.85 * x + 0.04 * y
            yn = -0.04 * x + 0.85 * y + 1.6

        x, y = xn, yn

        xr = int(scale * (x + 2.1818))
        yr = HEIGHT - int(scale * y)

        pixel(GREEN, (xr, yr))
    update()
