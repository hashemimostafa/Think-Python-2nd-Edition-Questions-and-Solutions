# =============================================================================
# The mathematician Srinivasa Ramanujan found an infinite series that 
# can be used to generate a numerical approximation of 1/π:
# ******
# Write a function called estimate_pi that uses this formula to compute and 
# return an estimate of π. It should use a while loop to compute terms of 
# the summation until the last term is smaller than 1e-15 
# (which is Python notation for 10 − 15 ). You can check the result by 
# comparing it to math.pi.
# Solution: http://thinkpython2.com/code/pi.py .
# =============================================================================

import math

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

def  estimate_pi():
    sum = 0
    k = 0
    c = 2 * math.sqrt(2) / 9801    
    while True:
        i = c * (fac(4 * k) * (1103 + 26390 * k)) / (fac(k)**4 * 396**(4 * k))
        k = k + 1
        if i < 1e-15:
            break
        sum += i
        pi = 1 / sum
    return pi

print('Srinivasa Formula is: ', estimate_pi())

print('pi is ', math.pi)