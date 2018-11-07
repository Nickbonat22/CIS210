''' 
CIS 210 STYLE
CIS 210 F17 Project 1

Author: Nicholas Bonat

Credits: N/A

Add docstrings to Python functions implementing quiz 1 pseudocode.
'''

def q1(onTime, absent):
    '''(boolean, boolean) -> None

    Function q1 has two parameters: onTime and absent, which are both boolean.
    Depending on which parameter is True or False, a statement is printed. The
    return value is None.
    
    >>> q1(True, False)
    Hello!
    >>> q1(False, False)
    Better late than never.
    >>> q1(False, True)
    Is anyone there?
    >>> 
    '''
    if onTime:
        print('Hello!')
    elif absent:
        print('Is anyone there?')
    else:
        print('Better late than never.')

    return None

#q1(False, False)

def q2(age, salary):
    '''(int, int) -> boolean

    Function q2 has two integer parameters: age and salary. True of False is
    returned based on if age is less than 18 and salary is less than 10000
    
    >>> q2(18, 5000)
    False
    >>> q2(16, 5000)
    True
    '''
    return (age < 18) and (salary < 10000)

#print(q2(18, 5000))
#print(q2(16, 5000))

def q3():
    '''() -> int

    Function q3 has no parameters. The integer 6 is returned as 1 < 2, and
    2 isn't greater than 4.

    >>> q3()
    6
    '''
    p = 1
    q = 2
    result = 4
    if p < q:
        if q > 4:
            result = 5
        else:
            result = 6

    return result

#print(q3())

def q4(balance, deposit):
    '''(int, int) -> int

    Function q4 has two parameters: balance and deposit which are both integers.
    With each loop the deposit is added to the total balance.
    
    >>> q4(0, 10)
    100
    >>> q4(100, 10)
    200
    >>> q4(10, 1)
    20
    '''
    count = 0
    while count < 10:
        balance = balance + deposit
        count += 1

    return balance

#print(q4(100, 10))

def q5(nums):
    '''(list of ints) -> int

    Function q5 takes numbs as a parameter which is a list of integers.
    Non-negative numbers in the list are counted and that number is returned.
    
    >>> q5([1,2,3,4,5,5,-1])
    6
    >>> q5([-1,-4])
    0
    >>> q5([-1,-4,2,2,4])
    3
    '''
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            result += 1

        i += 1

    return result

#print(q5([0, 1, 2, 3, 4, 5]))
#print(q5([0, -1, 2, -3, 4, -5]))

def q6():
    '''() -> None

    Function q6 has no parameters and prints the result of a while loop. Every
    iteration p(int value of 1) is multiplied to 2 and set to the value p. 16
    is the final int. The function before fixing the bug was in an
    infinite loop as i is set to 1 everytime it loops.
    
    >>> q6()
    2-power is 16
    '''
    i = 0
    p = 1
    while i < 4:
        #bug
        #i = 1
        p = p * 2
        i += 1

    print('2-power is', p)
    return None

#q6()
