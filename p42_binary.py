'''
Binary Encoding and Decoding
CIS 210 F17 Project 4, Part 2

Author: Nicholas Bonat

Credits: Lab help for doctest.testmod

Convert a non-negative integer to binary and prints it. Then converts
back to decimal form and prints the value.
'''
import doctest

def dtob(n):
    '''(int) -> str

    Function dtob takes non-negative integer as a parameter and returns
    its binary representation.

    >>> dtob(27)
    '11011'
    >>> dtob(0)
    '0'
    >>> dtob(2)
    '10'
    '''   
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

def main():
    
    number = int(input("Enter a non-negative integer: "))
    
    binary = dtob(number)
    
    print(binary)
    
    decimal = btod(binary)
    
    print(decimal)
    
if __name__ == '__main__':
    doctest.testmod()

main()
