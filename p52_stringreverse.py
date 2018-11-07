'''
String Reversal
CIS 210 F17 Project 5, Part 2

Author: Nicholas Bonat

Credits: Lab help for hailstone function

Using recursive and iterative algorithms for reversing a string.
'''
import doctest

def strReverseR(s):
    '''(str) -> str

    This function strReverseR has one parameter, s. Using a recursive function,
    a string is reversed and returned.

    >>> strReverseR('hello, world') #basic use of function
    'dlrow ,olleh'
    >>> strReverseR('') #edge case
    ''
    >>> strReverseR(' ') #edge case
    ' '
    >>> strReverseR('21')
    '12'
    >>> strReverseR(1) #boundary case
    's must be a string'
    '''
    if type(s) == int:
        error = 's must be a string'
        return error
    
    if s == "":
        return s
    
    else:
        return strReverseR(s[1:]) + s[0]
    
def strReverseI(s):
    '''(str) -> str

    This function strReverseI has one parameter, s. Using an iterative function,
    a string is reversed and returned.

    >>> strReverseI('hello, world') #basic use of function
    'dlrow ,olleh'
    >>> strReverseI('') #edge case
    ''
    >>> strReverseI(' ')
    ' '
    >>> strReverseI('21')
    '12'
    >>> strReverseI(1) #boundary case
    's must be a string'
    '''
    if type(s) == int:
        error = 's must be a string'
        return error
    
    reverseS = ''

    for i in s:
        reverseS = i + reverseS
        
    return reverseS

def main():
    '''() -> None

    function main takes a user string and prints the string backwards
    using two methods.
    '''
    text = input('Enter a string to reverse: ')

    revR = strReverseR(text)
    print("Recursive reverse: {}".format(revR))

    revI = strReverseI(text)
    print("Iterative reverse: {}".format(revR))

    return None

if __name__ == '__main__':
    main()

doctest.testmod()

#EXTRA CREDIT
def hailstone(n):
    '''(int) -> None

    Function hailstone prints the integer that fits the hailstone sequence
    recursively until 1 is reached (not proven 1 is reach every time).
    
    >>> hailstone(5)
    5
    16
    8
    4
    2
    1
    '''

    print(int(n))
    
    if n % 2 == 0:
        hailstone(n / 2)
        
    elif n > 1:
        hailstone((n * 3) + 1)

    return None
