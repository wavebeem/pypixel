#!/usr/bin/python

from pypixel import *

def circles():
    hue = 0
    size = 10
    while True:
        for x in xrange(0, WIDTH + 1, size):
            for y in xrange(0, HEIGHT + 1, size):
                circle(hsv((hue, 100, 100)), (x, y), size)
                hue += 1
                hue %= 360
            update()

def lines():
    hue = 0
    width = 1
    for x in xrange(0, WIDTH + 1, width):
        line(hsv((hue, 100, 100)), (x, 0), (x, HEIGHT), width)
        update()
        hue += 1
    for x in reversed(xrange(0, WIDTH + 1, 1)):
        line(hsv((hue, 100, 100)), (x, 0), (x, HEIGHT), width)
        update()
        hue += 1
        hue %= 360

def transition():
    hue = 0
    size = WIDTH
    while True:
        for x in xrange(0, WIDTH + 1, size):
            for y in xrange(0, HEIGHT + 1, size):
                circle(hsv((hue, 100, 100)), (x, y), size)
                update()
                hue += 1
                hue %= 360

def random_circles():
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

def rainbow_random_circles():
    h = 0
    while True:
        x  = random(WIDTH)
        y  = random(HEIGHT)
        r  = random(1, 100)
        h += 1
        h %= 360
        s  = 100
        v  = 100
        c  = hsv((h, s, v))
        circle(c, (x, y), r)
        update()

run(rainbow_random_circles)
