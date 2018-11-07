'''                          
Fizzbuzz
CIS 210 F17 Project 1-2

Author: Nicholas Bonat

Credits: N/A

Print a number or word based on if that number is divisble by 3,5, or both.
'''
def fb(n):
    '''(int) -> None

    Print 1 through n with every number divisible by 3 printing fizz, every
    number divisible by 5 printing buzz, and every number divisible by 3 and
    5 printing fizzbuzz.

    >>> fb(0)
    Game Over!
    >>> fb(9)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    Game Over!
    >>> fb(15)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    Game Over!
    '''

    
    for i in range(1,n+1):
        
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
            
        elif i % 3 == 0:
            print("fizz")
            
        elif i % 5 == 0:
            print("buzz")
        
        else:
            print(i)
        
    print("Game Over!")

    return None
