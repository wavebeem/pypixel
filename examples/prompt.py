#!/usr/bin/python2

from pypixel import *

number_of_circles = int(raw_input("How many circles do you want? "))

title("User input demo")
show()

for n in xrange(number_of_circles):
    x = random(WIDTH)
    y = random(HEIGHT)
    point = (x, y)
    circle(WHITE, point, 10)

update()
