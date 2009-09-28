#!/usr/bin/python

from pypixel import *

show()

x = WIDTH  / 2
y = HEIGHT / 2
base_size = 25
w = base_size
h = base_size
move_scale = 5
size_scale = 5
while True:
    x += move_scale * (-1 if random(2) == 0 else +1)
    y += move_scale * (-1 if random(2) == 0 else +1)

    x %= WIDTH
    y %= HEIGHT


    w += size_scale * (-1 if random(2) == 0 else +1)
    h += size_scale * (-1 if random(2) == 0 else +1)

    w %= WIDTH
    h %= HEIGHT

    if w < base_size: w += base_size
    if h < base_size: h += base_size

    color = hsv((random(360), 100, 100))
    ellipse(color, ((x, y), (w, h)), center=True)
    update()
    ellipse(BLACK, ((x, y), (w, h)), center=True)
