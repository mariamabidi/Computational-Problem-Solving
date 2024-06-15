"""
CSCI-603: Vertex
Author: RIT CS

An implementation of a vertex as part of a graph.

Code taken from the online textbook and modified:

http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
"""

from typing import Any, Hashable


class Vertex:
    """
    An individual vertex in the graph.

    :slots: id:  The identifier for this vertex (user defined, typically
        a string)
    :slots: neighbors:  A dictionary of adjacent neighbors, where the key is
        the neighbor (Vertex), and the value is the edge cost (int)
    """

    __slots__ = '_id', '_neighbors'
    _id: Any
    _neighbors: dict['Vertex', int]

    def __init__(self, key: Any):
        """
        Initialize a vertex
        :param key: The identifier for this vertex
        :return: None
        """
        self._id = key
        self._neighbors = {}

    def add_neighbor(self, nbr: 'Vertex', weight: int = 0) -> None:
        """
        Connect this vertex to a neighbor with a given weight (default is 0).
        :param nbr: The neighbor vertex
        :param weight: The edge cost
        :return: None
        """
        self._neighbors[nbr] = weight

    def __str__(self) -> str:
        """
        Return a string representation of the vertex and its direct neighbors:

            vertex-id neighbors [neighbor-1-id, neighbor-2-id, ...]

        :return: The string
        """
        return str(self._id) + ' neighbors: ' + str([str(x._id) for x in self._neighbors])

    def get_neighbors(self):
        """
        Get the neighbor vertices.
        :return: A list of Vertex neighbors
        """
        return self._neighbors.keys()

    def get_id(self) -> Any:
        """
        Get the vertex id
        :return: the id
        """
        return self._id

    def get_weight(self, nbr: 'Vertex') -> int:
        """
        Get the edge cost to a neighbor.
        :param nbr: The neighbor vertex
        :return: The weight (int)
        """
        return self._neighbors[nbr]


def testVertex():
    """
    A test function for the Vertex class.
    :return: None
    """
    vertexA = Vertex('A')
    vertexB = Vertex('B')
    vertexC = Vertex('C')
    vertexD = Vertex('D')
    vertexA.add_neighbor(vertexB, 3)
    vertexA.add_neighbor(vertexC, 1)
    vertexB.add_neighbor(vertexA, 4)
    vertexB.add_neighbor(vertexC, 2)
    vertexC.add_neighbor(vertexD, 5)

    # test __str__()
    print(vertexA)
    print(vertexD)

    # test get_weight()
    print('A -> B weight (3):', vertexA.get_weight(vertexB))
    print('C -> D weight (5):', vertexC.get_weight(vertexD))

    # test get_neighbors():
    print("B's neighbors ():", [vertex.get_id() for vertex in vertexB.get_neighbors()])
    print("D's neighbors ():", list(vertexD.get_neighbors()))


if __name__ == '__main__':
    testVertex()