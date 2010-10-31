#!/usr/bin/python2

from pypixel import *
from math import *

show()

# Face
circle(YELLOW, (WIDTH/2, HEIGHT/2), HEIGHT/2)

# Left eye
circle(BLACK, (WIDTH/3, HEIGHT/4), HEIGHT/8)
circle(WHITE, (WIDTH/3, HEIGHT/4), HEIGHT/8 - 1)
circle(BLACK, (WIDTH/3, HEIGHT/4), HEIGHT/16)

# Right eye
circle(BLACK, (WIDTH - WIDTH/3, HEIGHT - HEIGHT*3/4), HEIGHT/8)
circle(WHITE, (WIDTH - WIDTH/3, HEIGHT - HEIGHT*3/4), HEIGHT/8 - 1)
circle(BLACK, (WIDTH - WIDTH/3, HEIGHT - HEIGHT*3/4), HEIGHT/16)

# Mouth
arc(BLACK, (CENTER, HEIGHT/2), 200, 340, 16)

update()
