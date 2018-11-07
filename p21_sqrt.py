'''                          
Approximate Square Root
CIS 210 F17 Project 2, Part 1

Author: Nicholas Bonat

Credits: N/A

Approximate the square root of a number using the math module sqrt and comparing
the result using an iterative algorithm.
'''
from math import sqrt

def sqrt_compare(num, iterations):
    '''(int, int) -> None

    Function sqrt_compare has two parameters: num and iterations, both integers.
    mysqrt is called to compare the value returned by the function with math
    module sqrt. The results are printed along with a percent error. None is
    returned.

    >>> sqrt_compare(10000, 8)
    For 10000 using 8 iterations:
    my_sqrt value is: 101.20218365353946 
    math lib sqrt is: 100.0 
    This is a  1.20 percent error.
    '''
    
    my_sqrt = mysqrt(num,iterations)
    
    lib_sqrt = sqrt(num)
    
    error = (my_sqrt-lib_sqrt)
    
    percent_error = (error/lib_sqrt) *100

    percent_error1 = ("%.2f" % percent_error) #contains error to 2 decimal places
    
    print ("For",num,"using",iterations,"iterations:\nmysqrt value is:",my_sqrt,
           "\nmath lib sqrt is:",lib_sqrt,
           "\nThis is a ",percent_error1,"percent error.\n")
    

def mysqrt(n, k):
    '''(int, int) -> float

    Function my_sqrt has two parameters: n and k, which are both positive ints.
    n is the int to find the square root of while k is the number of times the
    iterative square root approximation should run. The approximate square root
    is returned.
    
    >>> mysqrt(25, 5)
    5.000023178253949
    >>> mysqrt(25, 10)
    5.0
    >>> mysqrt(625, 10)
    25.0
    '''
    
    x = 1.0

    for index in range(k):
        x = 0.5 * (x + n / x)       

    return x
