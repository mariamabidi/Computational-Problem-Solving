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
from graph import Graph


class Simulation:
    """
    A class to make a graph and perform simulation on the graph.
    """
    __slots__ = "cowsPainted", "adjacencyList"
    _cowsPainted: dict
    _adjacencyList: dict

    def __init__(self, adjacencyList: dict):
        """
        The constructor
        :param adjacencyList: The adjacency List
        """
        self.adjacencyList = adjacencyList
        self.cowsPainted = {}

    def makeGraph(self):
        """
        A method to make graph from an adjacency list
        :return:
        """
        field = Graph()
        for state, neighbors in self.adjacencyList.items():
            for neighbor in neighbors:
                field.add_edge(state, neighbor)

        for state in field:
            print(state)

        return field

    def __simulation(self, start, vertice, visited, thePaintballs: dict, theCows: dict):
        """
        A recursive helper function for simulation
        :param start: the initial paintball triggered
        :param vertice: starting point
        :param visited: the visited vertices set
        :param thePaintballs: dictionary of paintballs
        :param theCows: dictionary of cows
        :return:
        """
        for neighbor in vertice.get_neighbors():
            if neighbor not in visited:
                if neighbor.get_id() in theCows:
                    toAdd = self.cowsPainted[str(start)]
                    for cows in toAdd:
                        if neighbor.get_id() in cows:
                            cows[neighbor.get_id()].add(vertice.get_id())
                    print("     " + str(neighbor.get_id()) + " is painted " + str(vertice.get_id()) + "!")
                elif neighbor.get_id() in thePaintballs:
                    visited.add(neighbor)
                    print("     " + str(neighbor.get_id()) + " is triggered by " + str(vertice.get_id()) + " paint ball")
                    self.__simulation(start, neighbor, visited, thePaintballs, theCows)

    def startSimulation(self, theField: Graph, thePaintball: dict, theCows: dict):
        """
        The simulation method which does depth first search on the graph provided.
        :param theField: The graph to traverse
        :param thePaintball: dictionary of paintballs
        :param theCows: dictionary of cows
        :return:
        """
        print("\nBeginning Simulation...")

        for vertices in theField:
            visited = set()
            visited.add(vertices)
            if vertices.get_id() in thePaintball:
                self.cowsPainted[vertices.get_id()] = []
                for keys in theCows:
                    self.cowsPainted[vertices.get_id()].append({keys: set()})
                print("Triggering " + str(vertices.get_id()) + " paint ball...")
                self.__simulation(vertices.get_id(), vertices, visited, thePaintball, theCows)

    def get_cowsPainted(self):
        """
        A getter for the cows painted dictionary
        :return: the cows painted dictionary
        """
        return self.cowsPainted
