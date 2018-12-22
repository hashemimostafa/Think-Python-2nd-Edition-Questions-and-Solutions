# =============================================================================
# The letters of the alphabet can be constructed from a moderate number of 
# basic elements, like vertical and horizontal lines and a few curves. 
# Design an alphabet that can be drawn with a minimal number of basic elements 
# and then write functions that draw the letters.
# You should write one function for each letter, with names draw_a, draw_b,
# etc., and put your functions in a file named letters.py. You can download
# a “turtle typewriter” from http://thinkpython2.com/code/typewriter.py
# to help you test your code.
# You can get a solution from http://thinkpython2.com/code/letters.py ;
# it also requires http://thinkpython2.com/code/polygon.py .
# 
# =============================================================================
from __future__ import print_function, division

import math
import turtle

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

# =========================Letters=============================================

def draw_a(t, size):
    angle = 70
    x = size * math.cos(angle * math.pi / 180)
    t.lt(angle)
    t.fd(size)
    t.rt(2 * angle)
    t.fd(size)
    t.pu()
    t.bk(size / 2)
    t.pd()
    t.rt(180 - angle)
    t.fd(x)

def draw_b(t, size):
    t.lt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size/8)
    arc(t, size/4, -180)
    t.fd(size/8)
    t.rt(180)
    t.fd(size/8)
    arc(t, size/4, -180)
    t.fd(size/8)

def draw_c(t, size):
    t.pu()
    arc(t, size, -30)
    t.rt(90)
    t.pd()
    arc(t, size, -300)

def draw_d(t, size):
    t.pu()
    t.fd(size)
    t.lt(90)
    t.pd()
    t.fd(2*size)
    t.bk(size)
    t.rt(270)
    t.fd(size/4)
    arc(t, size/2, 180)
    t.fd(size/4)

def draw_e(t, size):
    t.fd(size)
    t.bk(size)
    t.lt(90)
    t.fd(size)    
    t.rt(90)
    t.fd(size)
    t.bk(size)
    t.lt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size)

def draw_f(t, size):
    t.lt(90)
    t.fd(size)    
    t.rt(90)
    t.fd(size)
    t.bk(size)
    t.lt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size)

def draw_g(t, size):
    t.rt(180)
    t.fd(size/4)
    arc(t, size/2, -180)
    t.fd(size/4)
    t.rt(90)
    t.fd(3*size/2)
    arc(t, 3*size/8, -180)    

def draw_h(t, size):
    t.lt(90)
    t.fd(2*size)
    t.bk(size)
    t.rt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.bk(2*size)

def draw_i(t, size):
    t.lt(90)
    t.fd(2*size)

def draw_j(t, size):
    t.fd(size/8)
    t.bk(size/4)
    t.fd(size/8)
    t.rt(90)
    t.fd(3*size/2)
    arc(t, size/2, -180)

def draw_k(t, size):
    t.lt(90)
    t.fd(2*size)
    t.bk(size)
    t.rt(45)
    _ = size* math.sqrt(2)
    t.fd(_)
    t.bk(_)
    t.rt(90)
    t.fd(_)
        
def draw_l(t, size):
    t.fd(size)
    t.bk(size)
    t.lt(90)
    t.fd(2*size)

def draw_m(t, size):
    t.lt(90)
    t.fd(size)
    t.rt(135)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.rt(135)
    t.fd(size)
    
def draw_n(t, size):
    t.lt(90)
    t.fd(size)
    t.rt(135)
    t.fd(size*math.sqrt(2))
    t.lt(135)
    t.fd(size)
    
def draw_o(t, size):
    arc(t, size, 360)

def draw_p(t, size):
    t.fd(size/8)
    arc(t, size/2, 180)
    t.fd(size/8)
    t.lt(90)
    t.fd(2*size)
    
def draw_q(t, size):
    t.rt(180)
    t.fd(size/4)
    arc(t, size/2, -180)
    t.fd(size/4)
    t.rt(90)
    t.fd(2*size)    

def draw_r(t, size):
    t.fd(size/8)
    arc(t, size/2, 180)
    t.fd(size/8)
    t.lt(90)
    t.fd(2*size)
    t.bk(size)
    t.lt(45)
    t.fd(size*math.sqrt(2))

def draw_s(t, size):
    t.rt(90)
    arc(t, size, 270)
    arc(t, size, -270)

def draw_t(t, size):
    t.lt(90)
    t.fd(2*size)
    t.lt(90)
    t.fd(size)
    t.bk(2*size)

def draw_u(t, size):
    t.rt(90)
    t.fd(size)
    arc(t, size/2, 180)
    t.fd(size)

def draw_v(t, size):
    t.rt(60)
    t.fd(size)
    t.lt(120)
    t.fd(size)

def draw_w(t, size):
    t.rt(60)
    t.fd(3*size/2)
    t.lt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.lt(120)
    t.fd(3*size/2)

def draw_x(t, size):
    t.lt(60)
    t.fd(2*size)
    t.bk(size)
    t.lt(60)
    t.fd(size)
    t.bk(2*size)

def draw_y(t, size):
    t.lt(90)
    t.fd(size)
    t.rt(30)
    t.fd(size)
    t.bk(size)
    t.lt(60)
    t.fd(size)

def draw_z(t, size):
    t.fd(size)
    t.rt(135)
    t.fd(size*math.sqrt(2))
    t.lt(135)
    t.fd(size)
#--------------------typewriter--------------------
bob = turtle.Turtle()
# =============================================================================
# draw_a(bob, 100)
# draw_b(bob, 100)
# draw_c(bob, 100)
# draw_d(bob, 100)
# draw_e(bob, 100)
# draw_f(bob, 100)
# draw_g(bob, 100)
# draw_h(bob, 100)
# draw_i(bob, 100)
# draw_j(bob, 100)
# draw_k(bob, 100)
# draw_l(bob, 100)
# draw_m(bob, 100)
# draw_n(bob, 100)
# draw_o(bob, 100)
# draw_p(bob, 100)
# draw_q(bob, 100)
# draw_r(bob, 100)
# draw_s(bob, 100)
# draw_t(bob, 100)
# draw_u(bob, 100)
# draw_v(bob, 100)
# draw_w(bob, 100)
# draw_x(bob, 100)
# draw_y(bob, 100)
# draw_z(bob, 100)
# =============================================================================
