#!/usr/bin/python

from pypixel import *

def rainbow_random_rects():
    hue = 0
    while True:
        x  = WIDTH  / 4
        y  = HEIGHT / 4
        w  = random(WIDTH)  / 2
        h  = random(HEIGHT) / 2
        hue += 1
        hue %= 360
        sat  = 100
        val  = 100
        col  = hsv((hue, sat, val))
        rect = ((x, y), (w, h))
        rectangle(col, rect)
        update()

run(rainbow_random_rects)
