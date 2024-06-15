from typing import Any

__author__ = "CS RIT"

class QTNode:
    """
    Represents a Quadtree node in the tree for an image compressed using the Rich Image Tool file format.
    A node contains a value which is either a grayscale color (0-255) for a
    region, or quadtree.QUAD_SPLIT meaning this node cannot hold a single color
    and thus has split itself into 4 sub-regions (left, center-left, center-right, right).
    """
    __slots__ = "_value", "_ul", "_ur", "_ll", "_lr", "_level"
    _value: Any
    _ul: 'QTNode'
    _ur: 'QTNode'
    _ll: 'QTNode'
    _lr: 'QTNode'
    _level: int

    def __init__(self, value: Any, ul: 'QTNode' = None,
                 ur: 'QTNode' = None, ll: 'QTNode' = None, lr: 'QTNode' = None, level = 0):
        """
        Construct a quad tree node.
        :param value: the node's value
        :param ul: the node's upper left child
        :param ur: the node's upper right child
        :param ll: the node's lower left child
        :param lr: the node's lower right child
        """
        self._value = value
        self._ul = ul
        self._ur = ur
        self._ll = ll
        self._lr = lr
        self._level = level

    def get_level(self):
        return self._level

    def get_value(self) -> Any:
        """
        Get the node's value
        """
        return self._value

    def get_lower_left(self) -> 'QTNode':
        """
        Get the lower left quadrant node
        """
        return self._ll

    def get_lower_right(self) -> 'QTNode':
        """
        Get the lower right quadrant node
        """
        return self._lr

    def get_upper_left(self) -> 'QTNode':
        """
        Get the upper left quadrant node
        """
        return self._ul

    def get_upper_right(self) -> 'QTNode':
        """
        Get the upper right quadrant node
        """
        return self._ur

    def __str__(self):
        """
        Return the string representation of the node's value
        """
        return str(self._value)

    def set_level(self, value):
        """
        Setter for level
        """
        self._level = value

    def set_upper_left(self, value):
        """
        setter for the upper left quadrant
        """
        self._ul = value

    def set_upper_right(self, value):
        """
        setter for the upper right quadrant
        """
        self._ur = value

    def set_lower_left(self, value):
        """
        setter for lower left quadrant
        """
        self._ll = value

    def set_lower_right(self, value):
        """
        setter for lower right quadrant
        """
        self._lr = value

    def preorder(self, tree, elements = []):
        """
        A function to do preorder traversal.

        @param tree The node to traverse.
        """
        if tree:
            elements.append(tree.get_value())
            self.preorder(tree.get_upper_left(), elements)
            self.preorder(tree.get_upper_right(), elements)
            self.preorder(tree.get_lower_left(), elements)
            self.preorder(tree.get_lower_right(), elements)

        return elements

