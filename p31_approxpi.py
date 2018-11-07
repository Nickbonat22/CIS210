'''
Approximating Pi
CIS 210 F17 Project 3, Part 1

Author: Nicholas Bonat

Credits: Based on code on p.78 Miller and Ranum text.

This project will determine an approximate value of pi using the Monte Carlo
algorithm.
'''

import math
import random


def montePi(numDarts):
    '''(num) -> float

    numDarts is the parameter representing how many times the approximating
    pi process should run. This function will then return that approximation.

    >>> montePi(100)
    3.0
    >>> montePi(100000)
    3.143072
    '''

    circleCount = 0
    
    for i in range(numDarts):
        x = random.random()
        y = random.random()

        inCircle = isInCircle(x,y,1)
        
        if inCircle:
            circleCount = circleCount + 1

    pi = circleCount / numDarts * 4
           
    return pi

def isInCircle(x,y,r):
    '''(num) -> boolean

    The x and y parameters are the values of the point and r represents the
    radius. This function will return True if the input value is inside the
    circle and False if otherwise.

    >>> isInCircle(0,0,1)
    True
    >>> isInCircle(.5,.5,1)
    True
    >>> isInCircle(1,2,1)
    False
    '''

    if math.sqrt(x ** 2 + y ** 2) < r * r:
        return True
    
    return False
    
