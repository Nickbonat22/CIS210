'''
Testing Functions
CIS 210 F17 Project 6, Part 1

Author: Nicholas Bonat

Credits: 

Writing a function to test string reverse functions
'''
import p52_stringreverse as p5
import doctest

def test_reverse(f):
    '''(function) -> None

    Function test_reverse takes a function and reports if the tests cases
    are correct or not. None is returned.
    
    >>> test_reverse(p5.strReverseR)
    Checking() ... its value  is correct!
    Checking(a) ... its value a is correct!
    Checking(xyz) ... its value zyx is correct!
    Checking(testing123) ... its value 321gnitset is correct!
    Checking(hello, world) ... its value dlrow ,olleh is correct!
    '''
    testList = (('', ''),
                ('a', 'a'),
                ('xyz', 'zyx'),
                ('testing123', '321gnitset'),
                ('hello, world', 'dlrow ,olleh'))

    for i in testList:
        print('Checking({}) ... '.format(i[0]), end='')
        
        if f(i[0]) == i[1]:
            print('its value {} is correct!'.format(i[1]))
            
        else:
            print('Error: has wrong value {}, expected {}'.format(f(i[0]),i[1]))
        
    return None

def main():
    '''() -> None

    Function main calls string reverse test functions twice.
    '''
    print('Recursive testing:')
    test_reverse(p5.strReverseR)
    
    print('\n')
    
    print('Iterative testing:')
    test_reverse(p5.strReverseI)
    
    return None

#EXTRA CREDIT
def isMember(alist, target):
    '''(list of int, int) -> Boolean

    Function is_memberR has two parameters, alist and target, both integers.
    It will return True if target is an element of alist, and False if not. 

    >>> isMember([1,3,5,7],4) #even number of items
    False
    >>> isMember([23,24,25,26,27],5) #odd number of items 
    False
    >>> isMember([0,1,4,5,6,8],4) #even number of items
    True
    >>> isMember([0,1,2,3,4,5,6],3) #odd number of items
    True
    >>> isMember([1,3],1) #target is first item
    True
    >>> isMember([2,10],10) #target is last item
    True
    >>> isMember([99,100],101) #short list
    False
    >>> isMember([42],42) #one item
    True
    >>> isMember([43],44) #one item
    False
    >>> isMember([],99) #empty list
    False
    '''
    
    if len(alist) == 0:
        return False

    midpoint = (len(alist)) // 2
    middle = alist[midpoint]

    if middle == target:
        return True

    elif target < middle:
        alist = alist[:midpoint] 
        return isMember(alist, target)
    
    else:
        alist = alist[midpoint + 1:]  
        return isMember(alist,target)
    
    return True

if __name__=='__main__':
    main()

doctest.testmod()
