"""
cs_queue.py
author: CS RIT
description: A linked queue (FIFO) implementation
"""
from typing import Any

from cs_node import LinkedNode


class Queue:
    __slots__ = "_front", "_back", "name"
    _front: LinkedNode
    _back: LinkedNode
    _name = str

    def __init__(self, name: str) -> None:
        """ Create a new empty queue.
        """
        self._front = None
        self._back = None
        self.name = name

    def __str__(self) -> str:
        """ Return a string representation of the contents of
            this queue, oldest value first.
        """
        result = "Queue["
        n = self._front
        while n != None:
            result += " " + str(n.get_value())
            n = n.get_link()
        result += " ]"
        return result

    def is_empty(self) -> bool:
        return self._front == None

    def enqueue(self, newValue: Any) -> None:
        newNode = LinkedNode(newValue)
        if self._front == None:
            self._front = newNode
        else:
            self._back.set_link(newNode)
        self._back = newNode

    def dequeue(self) -> None:
        assert not self.is_empty(), "Dequeue from empty queue"
        self._front = self._front.get_link()
        if self._front == None:
            self._back = None

    def peek(self) -> Any:
        assert not self.is_empty(), "peek on empty queue"
        return self._front.get_value()

    put = enqueue
    remove = dequeue


# def test() -> None:
#     s = Queue()
#     print(s)
#     for value in 1, 2, 3:
#         s.enqueue(value)
#         print(s)
#     print("Dequeueing:", s.peek())
#     s.dequeue()
#     print(s)
#     for value in 15, 16:
#         s.insert(value)
#         print(s)
#     print("Removing:", s.peek())
#     s.remove()
#     print(s)
#     while not s.is_empty():
#         print("Dequeueing:", s.peek())
#         s.dequeue()
#         print(s)
#     print("Trying one too many dequeues... ", end="")
#     try:
#         s.dequeue()
#         print("Problem: it succeeded!")
#     except Exception as e:
#         print("Exception was '" + str(e) + "'")
#
#
# if __name__ == "__main__":
#     test()