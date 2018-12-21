# =============================================================================
# Write an appropriately general set of functions that can draw shapes 
# as in Figure 4.2.
# Solution: http://thinkpython2.com/code/pie.py .
# 
# =============================================================================
from __future__ import print_function, division

import math
import turtle

def pie(t, n, r):
    theta = 360/n
    a = 2 * r * math.sin(theta/2 * math.pi/180)
    t.rt(theta/2)
    for _ in range(n-1):
        t.fd(r)
        t.pu()
        t.bk(r)
        t.pd()
        t.rt(theta)
    
    t.fd(r)
    t.rt(90 + theta/2)
    for _ in range(n):
        t.fd(a)
        t.rt(theta)
        
bob = turtle.Turtle()
pie(bob, 7, 100)