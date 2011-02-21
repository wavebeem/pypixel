#!/usr/bin/python2

from pypixel import *

title("Fullscreen this. You need to see the border.")
show()

line(WHITE, (0, 0), (WIDTH-1, 0))
line(WHITE, (0, 0), (0, HEIGHT-1))
line(WHITE, (0, HEIGHT-1), (WIDTH-1, HEIGHT-1))
line(WHITE, (WIDTH-1, HEIGHT-1), (WIDTH-1, 0))

update()
pause()
