#!/usr/bin/python

def say(*xs):
    print " ".join([str(x) for x in xs])

def four(xs, f):
    for x in xs:
        f(x)

four([2**x for x in xrange(8)], say)
