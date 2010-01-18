#!/usr/bin/python

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
# arc(BLACK, ((WIDTH/2.5, WIDTH/2), (WIDTH/4, HEIGHT/6)), radians(200), radians(340), 8)
ellipse(BLACK, ((WIDTH/2, HEIGHT*6/10+20), (WIDTH/2, HEIGHT/2)), center=True)
rectangle(YELLOW, ((WIDTH/2, HEIGHT*6/10-20), (WIDTH/2, HEIGHT/3)), center=True)

update()
