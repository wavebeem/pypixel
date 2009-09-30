#!/usr/bin/python

from pypixel import *

show()

x = WIDTH  / 2
y = HEIGHT / 2
base_size = 25
w = base_size
h = base_size
sat = 0

def porm():
    if random(2) == 0:
        return -1
    else:
        return +1

while True:
    x += porm()
    y += porm()

    x %= WIDTH
    y %= HEIGHT


    w += porm()
    h += porm()

    w %= WIDTH
    h %= HEIGHT

    if w < base_size: w += base_size
    if h < base_size: h += base_size

    sat += 1
    sat %= 100

    color = hsv((0, sat, 100))
    ellipse(color, ((x, y), (w, h)), center=True)
    update()
    ellipse(BLACK, ((x, y), (w, h)), center=True)
