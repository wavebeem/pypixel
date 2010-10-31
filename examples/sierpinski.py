#!/usr/bin/python2

from pypixel import *

title("Sierpinski demo")
show()

vertices = [
    (WIDTH/2,        0), # Top
    (      0,   HEIGHT), # Bottom left
    (  WIDTH,   HEIGHT)  # Bottom right
]

point = CENTER

step_size = 250

while True:
    for i in xrange(step_size):
        vertex = vertices[random(0, 2)]
        point  = midpoint(vertex, point)
        pixel(YELLOW, point)
    update()
