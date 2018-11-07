'''
Who is in this class?
CIS 210 F17 Project 7, Part 1

Author: Nicholas Bonat

Credits: 

This project will use file processing and data analysis to find and report
the different majors represented in CIS 210.
'''
import p62_data_analysis as p6

def majors_readf(fname):
    '''(str) -> None

    Function majors_readf takes a file name as a str and returns a list of the
    majors in the file.

    #>>> majors_readf('majors_cis210f17.txt')
    *List of majors*
    '''

    with open(fname, 'r') as majorsf:
        
        listMajor = []
        
        for i in range(10):
            majorsf.readline()

        for i in majorsf:
            new = i.strip('\n')
            end = new.split()
            listMajor.append(end[0])
             
    return listMajor

def majors_analysis(majorsli):
    '''(list of str) -> list of str

    Function majors_analysis takes a list of str and returns a list with the
    most frequent item.

    >>> majors_analysis(['CIS','GS','CIS'])
    ['CIS']
    '''
    mode = p6.mode(majorsli)

    return mode

def majors_report(majors_mode, majorsli):
    '''(list of str, list of str) -> None

    Function majors_report takes two parameters, both lists of str and
    displays the content of the lists calling a function from p6. None is
    returned.

    >>> majors_report(['CIS'],['CIS','PS','CH','SDSC','CIS'])
    Most represented major(s):
    CIS
    ITEM   FREQUENCY
    CIS    2        
    CH     1        
    PS     1        
    SDSC   1
    '''
    print('Most represented major(s):')
    for item in majors_mode:
          print(item)

    freqTable = p6.frequencyTable(majorsli)

    print(freqTable)
    
    return None

def main():
    '''()-> None

    Calls: majors_readf, majors_analysis, majors_report
    Top level function for analysis of CIS 210 majors data. Returns None.
    
    > majors_main()
    '''
    #fname = 'majors_short.txt'
    fname = 'majors_cis210f17.txt'
    
    majorsli = majors_readf(fname)
    majors_mode = majors_analysis(majorsli)
    majors_report(majors_mode, majorsli)

    return None

if __name__ == '__main__':
    main()
