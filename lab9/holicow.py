__author__ = 'MA'
"""
CSCI-603 Lab 9: Holi Cow 

A program to represent a field with cows and paint balls as vertices and builds
a graph with the information, which paint ball triggers which paint ball and
colors which cow. 
It gives us the information that triggering which paint ball will be the most
beneficial.

Author: Mariam Abidi
"""
import sys
import math
from simulation import Simulation


def adjacencyList(theCows, thePaintballs):
    """
    This is a method to build an adjacency list.
    :param theCows: Dictionary with cow information
    :param thePaintballs: Dictionary with paintballs information
    :return: The adjacency list
    """
    theField = {}

    for keys in thePaintballs:
        theField[keys] = []
        coordinates = thePaintballs[keys][:2]
        splashRadius = thePaintballs[keys][-1]

        for items in thePaintballs.items():
            if keys not in items:
                alldimensions = items[1]
                newcoords = alldimensions[:2]
                distance = math.sqrt(abs((int(coordinates[0]) - int(newcoords[0]))) ** 2
                                     + abs((int(coordinates[1]) - int(newcoords[1])) ** 2))
                if distance <= float(splashRadius) :
                    theField[keys].append(items[0])

        for items in theCows.items():
            alldimensionsOfCows = items[1]
            newCoordsOfCows = alldimensionsOfCows[:2]
            distance = math.sqrt(abs((int(coordinates[0]) - int(newCoordsOfCows[0]))) ** 2
                                 + abs((int(coordinates[1]) - int(newCoordsOfCows[1]))) ** 2)
            if distance <= float(splashRadius):
                theField[keys].append(items[0])

    for keys in theCows:
        theField[keys] = []

    return theField


def readFile():
    """
    This method is used to read the file provided
    :return: The cow and paintball information
    """
    theCows = {}
    thePaintballs = {}
    try:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
            with open(filename) as f:
                for lines in f:
                    words = lines.split()
                    if words[0] == "cow":
                        theCows[words[1]] = words[2:]
                    elif words[0] == "paintball":
                        thePaintballs[words[1]] = words[2:]
            print("Number of vertices: " + str(len(theCows) + len(thePaintballs)) + " cows: " + str(len(theCows))
                  + " paint balls: " + str(len(thePaintballs)))
            print("--------------------------------------------------")
            return theCows, thePaintballs
        else:
            print("Usage:  python3 holicow.py {filename}")
    except FileNotFoundError:
        print("File Not Found: " + str(sys.argv[1]))


def results(resultDict: dict):
    """
    This method is used to get the results information
    :param resultDict: The dictionary containing the whole result
    :return: The highest number of paintballs triggers
    """
    counter = 0
    result = dict()
    for key, value in resultDict.items():
        for cows in value:
            for key2, value2 in cows.items():
                counter += len(value2)
                result[key] = counter
        counter = 0

    max_key = max(result, key=result.get)
    max_value = result[max_key]
    return max_key, max_value


def main():
    """
    The main function
    :return:
    """
    print("Field of Dreams")
    theCows, thePaintballs = readFile()
    theField = adjacencyList(theCows, thePaintballs)
    mySimulation = Simulation(theField)
    myGraph = mySimulation.makeGraph()
    mySimulation.startSimulation(myGraph, thePaintballs, theCows)
    cowPaintedData = mySimulation.get_cowsPainted()
    simulationResults = results(cowPaintedData)
    if simulationResults[1] == 0:
        print("\nOops!\nNo cows were painted by any starting paint ball!")
    else:
        print("\nResults:\nTriggering the " + str(simulationResults[0]) + " paint ball is the best choice with "
          + str(simulationResults[1]) + " total paint on the cows:")
        resultData = cowPaintedData[simulationResults[0]]
        for data in resultData:
            for key, value in data.items():
                formatted_value = '{}' if not value else value
                print(f"    {key}   {formatted_value}")


# Main Conditional Guard
if __name__ == '__main__':
    main()
