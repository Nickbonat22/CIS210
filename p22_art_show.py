'''                          
Art Show
CIS 210 F17 Project 2, Part 2

Author: Nicholas Bonat

Credits: N/A

Draw using turtle graphics.
'''

from turtle import *


def art_show(length, height):
    '''(number, number) -> None

    This function will create the Russian Flag using turtle graphics.
    The parameters length and height determine how wide and tall the
    flag will be. The returned value is None.

    >>> art_show(380,200)
    '''
    up()
    x = -150
    y = 150

    #drawing rectangle
    setpos(x,y)
    down()
    forward(length)
    right(90)
    forward(height)
    right(90)
    forward(length)
    right(90)
    forward(height)
    speed(0)
    
    return None

def draw_stripes(length,height):
    '''(number, number) -> None

    This function will create the Russian Flag using turtle graphics.
    The parameters length and height will create the stripes in the flag.
    The returned value is None.

    >>> draw_stripes(380,66.66666)
    '''
    
    #drawing and coloring strips
    fillcolor("blue")
    begin_fill()
    back(height)
    right(90)
    forward(length)
    right(90)
    forward(height)
    left(90)
    back(length)
    end_fill()

    fillcolor("red")
    begin_fill()
    right(90)
    forward(height)
    left(90)
    forward(length)
    left(90)
    forward(height)
    end_fill()

    hideturtle()

    return None

#drawing the flag
art_show(380,200)
draw_stripes(380,66.66666)
