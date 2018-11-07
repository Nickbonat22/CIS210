








def rainfall(f):
    '''
    '''
    raindict = {}
    day = 1
    
    with open(f, 'r') as page:
        for i in range(10):
           page.readline()

        for line in page:
            new = line.split(',')
            #print(new)
            raindict[day] = new
            day += 1
            

        return raindict.keys()
            
    
