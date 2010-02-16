#!/usr/bin/python

from pypixel import *

class Star:
    '''This class represents a star in the screensaver'''
    MAX_SPEED = 8
    MAX_SIZE  = 8

    def __init__(self, layer, pos):
        '''Stores the layer and position for the star'''
        self.layer = layer
        self.x, self.y = 0, pos

    @property
    def color(self):
        '''Returns the appropriate color based on layer so stars look closer
        or farther away'''
        return hsv((0, 0, self.brightness))

    @property
    def brightness(self):
        '''Returns the brightness of the star, based on layer'''
        return (2**(-(self.layer - 1))) * 100

    @property
    def speed(self):
        '''Returns speed based on layer for proper parallax (sp?) effect'''
        return Star.MAX_SPEED / self.layer

    @property
    def size(self):
        return Star.MAX_SIZE / self.layer

    @property
    def pos(self):
        return (self.x, self.y)

    def move(self):
        '''Updates the star's position based on its speed'''
        self.x += self.speed

    def in_bounds(self):
        '''Checks if the star is within the bounds of the screen'''
        return 0 <= self.x <= WIDTH

    def render(self):
        '''Renders the star to the screen'''
        circle(self.color, self.pos, self.size)

def chance(percent):
    return random(100) < percent

# Bring up the main window
show()

stars = []
while True:
    for star in stars:
        star.move()
        star.render()
    stars = filter(lambda star: star.in_bounds(), stars)
    if chance( 5): stars.append(Star(1, random(HEIGHT)))
    if chance(10): stars.append(Star(2, random(HEIGHT)))
    if chance(20): stars.append(Star(3, random(HEIGHT)))
    if chance(35): stars.append(Star(4, random(HEIGHT)))
    update()
    clear()
