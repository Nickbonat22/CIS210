'''
Data Analysis
CIS 210 F17 Project 6, Part 2

Author: Nicholas Bonat

Credits: Based on code in Miller and Ranum text.

Implement and revise data analysis and visualization functions
'''
import doctest
from turtle import *

def mean(alist):
    '''(list of num) -> num

    This function mean has one parameter, alist. The returned value is the
    average value of the numbers in alist.

    >>> mean([1,3,4,5])
    3.25
    >>> mean([1,2,3,4,5])
    3.0
    >>> mean([1])
    1.0
    >>> mean([1.4,2.5,4.6,4.9,5])
    3.6799999999999997
    '''
    mean = sum(alist) / len(alist)
    
    return mean

def median(alist):
    '''(list of num) -> num

    Return median of alist (of len > 0).

    >>> median([5, 7, 1, 3]) # list with even number of items
    4.0
    >>> median([1, 2, 2, 3, 99]) # list with odd number of items
    2
    >>> median([99]) # list with 1 item
    99
    >>> median([0, 0, 0, 0]) # list with all same item (even number)
    0.0
    '''
    copyl = alist[:]
    copyl.sort()
    copylen = len(copyl)
    
    if isEven(copylen):
        rmid = copylen // 2
        lmid = rmid - 1
        medi = (copyl[lmid] + copyl[rmid]) / 2
    else:
        mid = copylen // 2
        medi = copyl[mid]

    return medi

def isEven(n):
    '''(num) -> boolean

    Return True if n is even,
    else return False

    >>> isEven(4)
    True
    >>> isEven(1)
    False
    >>> isEven(0)
    True
    '''
    return (n % 2) == 0


def mode(alist):
    '''(list of num) -> list of num(s)

    This function mode has one parameter, alist. mode calls genFrequencyTable
    to generate a dictionary that tracks the count of each item in alist. The
    returned value is a list of major(s).

    >>> mode([1,2,3,4,1])
    [1]
    >>> mode([1,2,1.2,1.2])
    [1.2]
    >>> mode([1,2,1.2,1.2,2])
    [2, 1.2]
    >>> mode([0])
    [0]
    '''
    
    freqDic = genFrequencyTable(alist)
    countlist = freqDic.values()
    maxcount = max(countlist)

    modelist = []

    for item in freqDic:
        if freqDic[item] == maxcount:
            modelist.append(item)
            
    return modelist

def frequencyTable(alist):
    '''(List of int) -> None

    This function frequencyTable has one parameter, alist, an int. A table is
    created from the data. The returned value is None.

    #>>>frequencyTable([1,2,4,5,3,2,1,2,3,4])
    ITEM FREQUENCY
    1       2
    2       3
    3       2
    4       2
    5       1
    '''
    
    itemlist = genFrequencyTable(alist)


    print('{: <6} {: <9}'.format('ITEM', 'FREQUENCY'))

    for item in itemlist:
        print('{: <6} {: <9}'.format(item, itemlist[item]))

    return None

def main():
    '''() -> None

    Function main will produce a frequency table and report the mean, median,
    and mode of the values for the quakes list.
    '''
    quakes = [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3, 4.2, 2.6, 4.3, 3.1, 4.8, 2.9,
          2.6, 2.7, 2.9, 2.7, 2.5, 5.1, 4.7, 5.1, 2.6, 5.3, 5.4, 4.4, 3.3,
          4.0, 3.1, 4.9, 4.8, 2.5, 3.1, 2.6, 2.8, 3.1, 4.8, 5.1, 4.8, 2.5,
          4.6, 5.1, 2.6, 5.0, 2.5, 3.2, 5.3, 5.5, 2.8, 4.5, 2.6, 6.7, 2.6,
          4.6, 4.6, 4.9, 2.5, 4.1, 2.6, 2.9, 4.9, 2.5, 4.8, 4.8, 2.7, 5.0,
          2.7, 2.8, 4.1, 2.8, 5.8, 2.5, 3.9, 2.5, 4.9, 5.0, 2.5, 3.2, 4.8,
          4.1, 5.1, 4.7, 2.6, 3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 4.4, 4.6, 5.7,
          4.5, 2.9, 3.3, 2.7, 2.8, 2.9, 6.0, 3.0, 5.3, 2.7, 4.3, 2.6, 2.8,
          4.4, 4.3, 4.7, 2.5, 4.9, 4.9, 2.5, 4.8, 4.4, 6.6, 3.3, 2.5, 5.0,
          4.2, 4.5, 2.6, 4.0, 3.3, 2.7, 2.9, 2.7, 2.9, 3.3, 2.5, 4.3, 3.2,
          4.6, 2.8, 2.7, 2.6, 3.1, 2.9, 4.2, 4.5, 4.5, 2.8, 4.7, 4.6, 4.2,
          2.8, 2.5, 4.5, 4.6, 2.8, 2.9, 2.7, 3.1, 2.6, 3.2, 5.2, 2.8, 3.2,
          2.6, 2.7, 5.2, 6.4, 4.2, 3.1, 2.9, 3.1, 4.3, 4.9, 5.2, 2.7, 4.9,
          3.0, 4.9, 4.7, 2.5, 3.2, 2.7, 6.2, 4.0, 2.5, 5.1, 3.3, 2.5, 4.7,
          3.1, 4.6, 2.8, 3.1, 6.3]
    
    listmean = mean(quakes)
    listmedian = median(quakes)
    mostfreq = mode(quakes)

    itemlist = genFrequencyTable(quakes)

    print('Mean quake:')
    print("{:.1f}".format(listmean))
    print('Median quake:')
    print(listmedian)
    print('Most represented quake(mode):')
    print(mostfreq[0])
    print("ITEM","FREQUENCY")
    
    for item in itemlist:
        print(item,'   ',itemlist[item])
        
    return None

    
#EXTRA CREDIT
def frequencyChart(alist):
    '''(List of int) -> None

    This function frequencyChart has one paremeter, alist, an int. It will
    create a chart using turtle graphics with the data. The returned
    value is None.

   # >>> frequencyChart([1,2,4,5,3,2,1,2,3,4])
    turtle graphics of a chart displaying data
    '''

    itemlist = genFrequencyTable(alist)
    item = list(itemlist.keys())
    minitem = 0
    maxitem = len(item) - 1

    countlist = itemlist.values()
    maxcount = max(countlist)

    wn = Screen()
    wn.setworldcoordinates(-1,-1,maxitem+1,maxcount+1)
    hideturtle()

    up()
    goto(0,0)
    down()
    goto(maxitem,0)
    up()

    goto(-1,0)
    write("0",font=("Helvetica",16,"bold"))
    goto(-1,maxcount)
    write(str(maxcount),font=("Helvetica",16,"bold"))

    for index in range(len(item)):
        goto(index,0)
        write(str(item[index]),font=("Helvetica",16,"bold"))

        goto(index,0)
        down()
        goto(index,itemlist[item[index]])
        up()
    wn.exitonclick()

    return None
    
def genFrequencyTable(alist):
    '''(List of num or Strings) -> dicitonary of num or Strings

    This function genFrequencyTable has one parameter, alist. This will
    create a dicitonary from an input list of numbers and will be called in two
    other functions, frequencyTable and frequencyChart. The returned value is
    the dicitonary, countdict, an int.

    Commented out tests because order of return varies
    #>>> genFrequencyTable([2,4,6,8,2])
    {8: 1, 2: 2, 4: 1, 6: 1}
    #>>> genFrequencyTable(['CIS','MATH','CIS'])
    {'MATH': 1, 'CIS': 2}
    '''
    '''
    countdict = {}
    
    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item] + 1
        else:
            countdict[item] = 1

    return countdict
    '''
    
    freqD = {}

    for item in alist:
        freqD.setdefault(item, 0)
        freqD[item] += 1

    return freqD

if __name__ == '__main__':
    main()

doctest.testmod()
