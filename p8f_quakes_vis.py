'''
World-wide Earthquake Watch
CIS 210 F17 Project 8-f

Author: Nicholas Bonat

Credits: Based on code in Miller and Ranum text.

This project will use file processing and data mining to plot earthquake
activity around the world on a world map.
'''

from math import *
import turtle
import random

def readfile(file):
    '''(filename) -> dict of num

    Function readfile takes a file as a parameter and returns a dict with
    earthquake lat and log coordinates as the values.

    >>> readfile('earthquakesShort.txt')
    {1: [129.2695, 36.0645, 5.4]}
    '''
    with open(file, 'r') as myf:
        myf.readline()
        datadict = {}
        key = 0
        for line in myf:
            values = line.split(',')
            key += 1
            lat = float(values[1])
            lon = float(values[2])
            mag = float(values[4])
            datadict[key] = [lon, lat, mag]
            
    return datadict

def euclidD(point1, point2):
    '''
    (num,num) -> float

    This function euclidD has two parameters, point1 and point2. The distance
    of the two points is found and returned.

    >>> euclidD((1,0),(2,1))
    1.414213562370951
    '''
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total += diff

    euclidDistance = sqrt(total)

    return euclidDistance

def createCentroids(k, datadict):
    '''(num,dictionary of num) -> list of num

    This function createCentroids has two parameters, k and datadict. A list is
    created using the random module. The returned value is the list.
    
    >>> createCentroids(2,{-120.44,50})
    [98,44]
    '''
    centroids = []
    count = 0
    centroid_keys = []

    while count < k:
        rkey = random.randint(1, len(datadict))
        if rkey not in centroid_keys:
            centroids.append(datadict[rkey])
            centroid_keys.append(rkey)
            count += 1

    return centroids

def createClusters(k, centroids, datadict, iterations):
    '''(num,list of num, dictionary of num, num) -> list of num

    This function createClusters has four parameters: k, centroidsm datadict,
    and repeats. A list is created and returned.

    >>> createClustes(2,[-120.43,55],{-120.43},3)
    [70,50]
    '''
    for iteration in range(iterations):
       #print("****Iteration", iteration, "****")

        #creating a list and appending the correct coordinates
        clusters = []
        for i in range(k):
            clusters.append([])

        for key in datadict:
            distances = []
            for cl_index in range(k):
                dist = euclidD(datadict[key], centroids[cl_index])
                distances.append(dist)
            min_dist = min(distances)
            index = distances.index(min_dist)
            clusters[index].append(key)

        dimensions = len(datadict[1])
        for cl_index in range(k):
            sums = [0]*dimensions
            for key in clusters[cl_index]:
                data_points = datadict[key]
                for ind in range(2):
                    sums[ind] = sums[ind] + data_points[ind]
            for ind in range(len(sums)):
                cl_len = len(clusters[cl_index])
                if cl_len != 0:
                    sums[ind] /= cl_len
            centroids[cl_index] = sums

        #too much data to print
        """for c in clusters:
            print("CLUSTER")
            for key in c:
                print(datadict[key], end=" ")
            print()"""

    return clusters


def visualizeQuakes(k, r, dataFile):
    '''(num,num,filename) -> None

    Function visualizeQuakes takes two numbers and a filename as a parameter.
    All the functions are called.

    >>> visualizeQuakes(6,7,'earthquakes.txt')
    *worldmap gif with points being plotted*
    '''
    datadict = readfile(dataFile)
    quakeCentroids = createCentroids(k, datadict)
    clusters = createClusters(k, quakeCentroids, datadict, r)
    eqDraw(k, datadict, clusters)
    
    return None

def eqDraw(k, eqDict, eqClusters):
    '''(dict, list of num) -> None

    Function eqDraw takes the earthquake data dictionary and the list of
    clusters as parameters. Turtle graphics plots the earthquake points on a
    world map. None is returned
    '''
    quakeT = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic("worldmap.gif")
    quakeWin.screensize(1800, 900)

    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90

    quakeT.hideturtle()
    quakeT.up()
    quakeT.speed('fastest')

    colorlist = ['red', 'green', 'blue', 'orange', 'cyan', 'yellow']

    #assigning a color to a dot and plotting to a specific location
    for clusterIndex in range(k):
        quakeT.color(colorlist[clusterIndex])
        for key in eqClusters[clusterIndex]:
            lon = eqDict[key][0]
            lat = eqDict[key][1]
            quakeT.goto(lon * wFactor, lat * hFactor)
            quakeT.dot()
    quakeWin.exitonclick()

    return None
    
def main():
    '''() -> None

    Calls visualizeQuakes to access the file and plot points on the world map.
    '''
    k = 6
    r = 7
    f = 'earthquakes.txt'
    visualizeQuakes(k, r, f)

    return None

if __name__ == '__main__':
    main()
