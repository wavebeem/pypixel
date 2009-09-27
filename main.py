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
        r  = random(50, 100)
        h += 1
        h %= 360
        s  = 100
        v  = 100
        c  = hsv((h, s, v))
        circle(c, (x, y), r)
        update()

def rotating_line():
    angle   = 0
    x1      = WIDTH  / 2
    y1      = HEIGHT / 2
    radius  = HEIGHT
    red     = rgb((255, 0, 0))
    black   = rgb((0,   0, 0))
    while True:
        x2 = radius * cos(angle) + x1
        y2 = radius * sin(angle) + y1
        line(red, (x1, y1), (x2, y2))
        update()
        line(black, (x1, y1), (x2, y2))

        angle += 1

def rotating_lines():
    angle   = 0
    x1      = WIDTH  / 2
    y1      = HEIGHT / 2
    radius  = HEIGHT
    while True:
        x2 = radius * cos(angle) + x1
        y2 = radius * sin(angle) + y1
        line(RED, (x1, y1), (x2, y2))
        update()
        line(BLACK, (x1, y1), (x2, y2))

        x2 = radius * cos(-angle) + x1
        y2 = radius * sin(-angle) + y1
        line(GREEN, (x1, y1), (x2, y2))
        update()
        line(BLACK, (x1, y1), (x2, y2))

        angle += 1

run(rainbow_random_circles)
