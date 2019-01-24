# =============================================================================
# Exercise 5.5.
# Read the following function and see if you can figure out what it does 
# (see the examples in Chapter 4). Then run it and see if you got it right.
# Exercise 5.6. 
# The Koch curve is a fractal that looks something like Figure 5.2. 
# To draw a Koch curve with length x, all you have to do is
# 1. Draw a Koch curve with length x/3.
# 2. Turn left 60 degrees.
# 3. Draw a Koch curve with length x/3.
# 4. Turn right 120 degrees.
# 5. Draw a Koch curve with length x/3.
# 6. Turn left 60 degrees.
# 7. Draw a Koch curve with length x/3.
# The exception is if x is less than 3: in that case, you can just draw 
# a straight line with length x. 
# 1. Write a function called koch that takes a turtle and a length as 
# parameters, and that uses the turtle to draw a Koch curve with 
# the given length.
# 2. Write a function called snowflake that draws three Koch curves to make 
# the outline of a snowflake.
# Solution: http://thinkpython2.com/code/koch.py .
# 3. The Koch curve can be generalized in several ways. 
# See http://en.wikipedia.org/wiki/Koch_snowflake 
# for examples and implement your favorite.
# =============================================================================

import turtle
import math

def numbering(li, n):
    if n == 0:
        return li
    else:
        k = 1
        for i in range(len(li)):
            li.insert(k + 3 * i, 1)
            li.insert(k + 1 + 3 * i, 2)
            li.insert(k + 2 + 3 * i, 1)
            k += 1
        return numbering(li, n-1)

def Koch_snowflake(t, n, length):
    l = numbering([2, 2, 2], n)
    a = length / 3 ** n
    for i in range(len(l)):
        if l[i] == 1:
            t.fd(a)
            t.rt(60)
        elif l[i] == 2:
            t.fd(a)
            t.lt(120)
        else:
            pass
    
t = turtle.Turtle()
n = 4
length = 300
Koch_snowflake(t, n, length)
