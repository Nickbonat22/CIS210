'''
Who is in this class?
CIS 210 F17 Project 7, Part 2

Author: Nicholas Bonat

Credits: 

This project will use file processing and data analysis to report about
earthquakes in Eugene over the past 100 years.
'''
import p62_data_analysis as p6

def equake_readf(fname):
    '''(str) -> list of num

    Function equake_readf takes a txt file name as a string and returns
    a list the earthquake magnitudes. 

    >>> equake_readf('equake50f.txt')
    [5.2, 5.1, 6.0, 5.9, 5.6, 5.7, 5.0, 5.0, 5.2, 5.1, 5.4, 5.2, 5.6]
    '''
    mags = []
    
    with open(fname, 'r') as page:
        for i in range(10):
            page.readline()

        for line in page:
            test = line.strip()
            newline = test.split(',')
            mags.append(float(newline[4]))       
        
    return mags

def equake_analysis(magnitudes):
    '''(list) -> tuple

    Function equake_analysis takes a list of earthquakes and returns the mean,
    median, and mode of the data in a tuple.

    >>> equake_analysis([5.2, 5.1, 6.0, 5.9, 5.6, 5.7, 5.0, 5.0, 5.2, 5.1, 5.4])
    (5.381818181818183, 5.2, [5.1, 5.2, 5.0])
    '''
    mean = p6.mean(magnitudes)
    median = p6.median(magnitudes)
    mode = p6.mode(magnitudes)

    data = (mean, median, mode)

    return data

def equake_report(mmm, magnitudes):
    '''() -> None

    Function equake_report takes a tuple and list of earthquakes as parameters.
    The data is printed and None is returned.

    >>> equake_report((5.381818181818183, 5.2, [5.1, 5.2, 5.0]),[5.2, 5.1, 6.0, 5.9, 5.6, 5.7, 5.0, 5.0, 5.2, 5.1, 5.4])
    Earthquake Data Analysis
    E25 Years Ago to Present
    250km centered at Eugene, OR

    There have been 11 earthquakes over the past 25 years

    Mean magnitude is: 5.381818181818183
    Median magnitude is: 5.2
    Mode(s) magnitude is: [5.1, 5.2, 5.0]
    ITEM   FREQUENCY
    5.4    1        
    5.6    1        
    6.0    1        
    5.7    1        
    5.1    2        
    5.2    2        
    5.0    2        
    5.9    1 
    '''
    print('Earthquake Data Analysis')
    print('E25 Years Ago to Present')
    print('250km centered at Eugene, OR\n')
    print('There have been {} earthquakes over the past 25 years'.format(len(magnitudes)))
    print('\nMean magnitude is: {}'.format(mmm[0]))
    print('Median magnitude is: {}'.format(mmm[1]))
    print('Mode(s) magnitude is: {}'.format(mmm[2]))

    freqTable = p6.frequencyTable(magnitudes)
    print(freqTable)
    
    return None
    

def main():
    '''()-> None

    Calls: equake_readf, equake_analysis, equake_report
    
    Top level function for earthquake data analysis. Returns None.
    '''
    fname = 'equakes50f.txt'
    #fname = 'equakes25f.txt'
    #fname = 'equakes_short.txt'
    emags = equake_readf(fname)
    mmm = equake_analysis(emags)
    equake_report(mmm, emags)
    
    return None

main()
