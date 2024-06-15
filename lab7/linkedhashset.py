__author__ = 'MA'
"""
CSCI-603 Lab 7: LinkedHashTable 

A program to store values in a linked hash table and can remember the insertion
order of the values.

Author: Mariam Abidi
"""
from collections.abc import Iterable
from set import SetType
from typing import Any


class ChainNode:
    """
    A class to create nodes with three links -
    prev = previous element inserted
    next = next element inserted
    fwd = next element in the hash table
    """
    __slots__ = "_obj", "_prev", "_next", "_fwd"
    obj: Any
    prev: 'ChainNode'
    next: 'ChainNode'
    fwd: 'ChainNode'

    def __init__(self, _obj: Any, _prev: 'ChainNode' = None, _next: 'ChainNode' = None, _fwd: 'ChainNode' = None):
        self._obj = _obj
        self._prev = _prev
        self._next = _next
        self._fwd = _fwd

    def __repr__(self):
        return repr(self._obj) + " --> " + repr(self._fwd)

    def __str__(self):
        return self._obj

    def get_obj(self):
        """
        A method to get the object value.
        """
        return self._obj

    def get_prev(self):
        """
        A method to get the previous value.
        """
        return self._prev

    def get_next(self):
        """
        A method to get the next value
        """
        return self._next

    def get_fwd(self):
        """
        A method to get the next value in hash table
        """
        return self._fwd

    def set_prev(self, value: 'ChainNode' = None):
        """
        A method to set the previous value.
        @param value element to add
        """
        self._prev = value

    def set_next(self, value: 'ChainNode' = None):
        """
        A method to set the next value
        @param value element to add
        """
        self._next = value

    def set_fwd(self, value: 'ChainNode' = None):
        """
        A method to set the forward value.
        @param value element to add
        """
        self._fwd = value

    def __iter__(self):
        """
        An iterator for the ChainNode class
        """
        start = self._obj
        while start is not None and self is not None:
            yield self
            self = self._fwd


def default_hash_func(value: Any = None, table_capacity: int = 10):
    """
    Using the in-built hash function by default
    @param value element to add
    @param table_capacity number of buckets in hash table
    """
    return hash(value) % table_capacity


class LinkedHashSet(SetType, Iterable):
    """
    A class to create a Linked Hash Table that behaves like a set.
    """
    __slots__ = "HashSet", "initial_num_bucket", "load_limit", "hash_function", "front", "back"
    HashSet: list
    initial_num_bucket: int
    load_limit: float
    hash_function: Any
    _front: ChainNode = None
    _back: ChainNode = None

    def __init__(self, initial_num_buckets: int = 100, load_limit: float = 0.75,
                 hash_function: Any = default_hash_func):
        """
        The constructor for LinkedHashSet class.
        """
        super().__init__()
        if initial_num_buckets < 10:
            self.HashSet = [None] * 10
        else:
            self.HashSet = [None] * initial_num_buckets
        self.initial_num_bucket = initial_num_buckets
        self.load_limit = load_limit
        self.hash_function = hash_function
        self.initial_num_bucket = initial_num_buckets
        self.front = None
        self.back = None

    def __len__(self):
        """
        Returns the number of elements
        """
        return self.size

    def __repr__(self):
        return (f"Capacity: {self.initial_num_bucket} , Size: {self.size}, "
                f"Load Factor: {self.size / self.initial_num_bucket}, "
                f"Load Limit: {self.load_limit} \n {self.print_table()}")

    def print_table(self):
        """
        A method to print the whole table.
        """
        table = ""
        for index, bucket in enumerate(self.HashSet):
            table += str(index) + ": " + bucket.__repr__() + "\n "
        return table

    def __iter__(self):
        """
        An iterator for the LinkedHashSet class
        """
        start = self.front
        while start is not None and self is not None:
            yield start
            start = start.get_next()

    def __str__(self):
        """
        String representation of the class
        """
        table = "{ "
        for i in self:
            if i:
                table += str(i) + ", "
        return table + " }"

    def add(self, value: Any):
        """
        A method to add elements inside the Linked Hash Set.
        @param value The element to add
        """
        index_value = self.hash_function(value)
        if self.size == 0:
            new_node = ChainNode(value)
            self.front = new_node
            self.back = new_node
            self.HashSet[index_value] = new_node
            self.size += 1
            self.performRehash()
            return True
        else:
            if self.HashSet[index_value] is not None:
                for nodes in self.HashSet[index_value]:
                    if nodes is not None and nodes.get_obj() != value:
                        if nodes.get_fwd() is None:
                            newChainNode = ChainNode(value, self.back, None, None)
                            self.back.set_next(newChainNode)
                            nodes.set_fwd(newChainNode)
                            self.back = newChainNode
                            self.size += 1
                            self.performRehash()
                            return True
            else:
                new_node = ChainNode(value, self.back)
                self.back.set_next(new_node)
                self.back = new_node
                self.HashSet[index_value] = self.back
                self.size += 1
                self.performRehash()
                return True
        return False

    def contains(self, value: Any):
        """
        A method to check if the table contains an element.
        @param value The element to check
        """
        index_value = self.hash_function(value)
        if self.HashSet[index_value] is not None:
            for nodes in self.HashSet[index_value]:
                if nodes.get_obj() == value:
                    return True
        return False

    def remove(self, value: Any):
        """
        A method to remove an element from the list
        @param value The element to remove
        """
        index_value = self.hash_function(value)
        if self.HashSet[index_value] is not None:
            for nodes in self.HashSet[index_value]:
                if nodes.get_obj() == value:

                    if nodes == self.front:
                        self.front = self.front.get_next()
                        if nodes.get_next() is not None:
                            nodes.get_next().set_prev(nodes.get_prev())
                    if nodes == self.back:
                        self.back = self.back.get_prev()
                        if nodes.get_prev() is not None:
                            nodes.get_prev().set_next(nodes.get_next())

                    if nodes == self.HashSet[index_value]:
                        self.HashSet[index_value] = nodes.get_fwd()
                        if nodes != self.front and nodes.get_next() is not None:
                            nodes.get_next().set_prev(nodes.get_prev())
                    else:
                        nodes.get_prev().set_next(nodes.get_next())
                        nodes.get_next().set_prev(nodes.get_prev())

                    self.size -= 1
                    self.performRehash()
                    return True

                if nodes.get_fwd() is not None:
                    if nodes.get_fwd().get_obj() == value:
                        nodes.get_fwd().get_prev().set_next(nodes.get_fwd().get_next())
                        if nodes.get_fwd() == self.back:
                            self.back = nodes
                            self.performRehash()
                            self.size -= 1
                        else:
                            nodes.get_fwd().get_next().set_prev(nodes.get_fwd().get_prev())
                            self.performRehash()
                            self.size -= 1
                        nodes.set_fwd(nodes.get_fwd().get_fwd())
                        return True
        return False

    def performRehash(self):
        """
        A method to perform the rehash
        """
        loading = self.size / self.initial_num_bucket
        if loading > self.load_limit:
            self.rehash(self.initial_num_bucket * 2)
        if loading < 1 - self.load_limit:
            self.rehash(self.initial_num_bucket // 2)

    def rehash(self, buckets: int):
        """
        A method to rehash.
        @param buckets the list size to keep.
        """
        m = LinkedHashSet(buckets, self.load_limit, self.hash_function)
        node = self.front

        while node is not None:
            node = node.get_next()
        self = m


def main():
    m = LinkedHashSet(10, 0.5)
    m.add("m")
    m.add("gm")
    m.add("g")
    m.add("dm")
    print(repr(m))
    m.remove("dm")
    m.contains("gm")
    print(len(m))
    print(repr(m))
    for i in m:
        print(i)


# def main():
#     m = ChainNode("a", ChainNode("b"), ChainNode("c"), ChainNode("h", _fwd=ChainNode("j")))
#     print(repr(m))


if __name__ == '__main__':
    main()
