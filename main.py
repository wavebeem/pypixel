#!/usr/bin/python

from pypixel import *

hue = 0
def next_color():
    global hue
    hue %= 360
    c = Color(0)
    c.hsva = (hue, 100, 100, 100)
    hue += 1
    return c

def circles():
    size = 100
    while True:
        for x in xrange(0, WIDTH + 1, size):
            for y in xrange(0, HEIGHT + 1, size):
                circle(next_color(), (x, y), size)

def lines():
    width = 1
    for x in xrange(0, WIDTH + 1, width):
        line(next_color(), (x, 0), (x, HEIGHT), width)
    for x in reversed(xrange(0, WIDTH + 1, 1)):
        line(next_color(), (x, 0), (x, HEIGHT), width)

def transition():
    size = WIDTH
    while True:
        for x in xrange(0, WIDTH + 1, size):
            for y in xrange(0, HEIGHT + 1, size):
                circle(next_color(), (x, y), size)

run(transition)
