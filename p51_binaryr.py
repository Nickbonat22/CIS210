'''
Binary Encoding and Decoding Recursively
CIS 210 F17 Project 5, Part 1

Author: Nicholas Bonat

Credits: 

Convert a non-negative integer to binary recursively and prints it. Then
converts back to decimal form and prints the value. 
'''
import doctest

def dtob(n):
    '''(int) -> str

    Function dtob takes non-negative integer as a parameter and returns
    its binary representation.

    >>> dtob(27) #basic example of use
    '11011'
    >>> dtobr(-1) #boundary test
    'n must be greater than or equal to 0'
    >>> dtob(0) #edge case
    '0'
    >>> dtob(2) #edge case
    '10'
    '''
    if type(n) == str:
        strError = 'n must be a integer'
        return strError
    
    if n < 0:
        error = 'n must be greater than or equal to 0'
        return error
    
    binary = ''
    
    if n == 0:
        return '0'
    
    while n > 0:
        b_remain = str( n % 2 )
        
        n = n // 2
        
        binary += b_remain

    binary = binary[::-1]

    return binary

def btod(b):
    '''(str) -> int

    Function btod takes a binary representation of an integer
    as input and returns the corresponding integer.

    >>> btod('0000')
    0
    >>> btod('1101')
    13
    >>> btod('111111')
    63
    '''
    decimal = 0
    
    power = len(b) - 1
    
    for char in b:
        num = int(char)
        decimal += ( num * ( 2 ** power) )
        power -= 1

    return decimal

def dtobr(n):
    '''(int) -> str

    Function dtobr ecursively converts an interger to a
    string of binary numbers.

    >>> dtobr(27) #basic example of use 
    '11011'
    >>> dtobr(-1) #boundary test
    'n must be greater than or equal to 0'
    >>> dtobr(0) #edge case
    '0'
    >>> dtobr(1) #edge case
    '1'
    >>> dtobr('2') #boundary case
    'n must be a integer'
    >>> dtobr(27888) #boundary case
    '110110011110000'
    '''
    if type(n) == str:
        strError = 'n must be a integer'
        return strError
    
    if n < 0:
        error = 'n must be greater than or equal to 0'
        return error
    
    if n == 0:
        return str(0)
    
    if n == 1:
        return str(1)
    
    r = n % 2
    b = n // 2
    
    return str(dtobr(b))+str(r)
    

def main():
    '''() -> None

    Function main checks binary conversion functions by encoding and decoding
    number
    '''
    
    number = int(input("Enter a non-negative integer: "))
    
    binary = dtob(number)
    binaryR = dtobr(number)
    
    print('Binary format is {}'.format(binary))
    print('Binary format recursively is {}'.format(binaryR))
    
    decimal = btod(binary)
    print('Back to decimal {}'.format(decimal))
    
    
if __name__ == '__main__':
    doctest.testmod()

main()
