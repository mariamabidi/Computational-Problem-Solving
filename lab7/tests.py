""" 
file: tests.py
description: Verify the LinkedHashSet class implementation
"""

__author__ = "Mariam Abidi"

from typing import Any

from src.linkedhashset import LinkedHashSet


def print_set(a_set):
    for word in a_set:  # uses the iter method
        print(word, end=" ")
    print()


def test0():
    """
    This test is a standard test
    """
    table = LinkedHashSet(20, 0.6)
    table.add("a")
    table.add("g")
    table.add("z")
    table.add("9")
    table.add("l")

    print_set(table)

    print("'z' in table?", table.contains("z"))
    table.remove("9")
    print("'t' in table?", table.contains("t"))

    print_set(table)
    print(table)
    print(repr(table))


def test1():
    """
    This test creates a very big table for some elements
    """
    table = LinkedHashSet(100, 0.3)
    table.add("a")
    table.add("aa")
    table.add("aaa")
    table.remove("ca")
    table.add("b")
    table.add("bb")
    table.remove("o")
    table.add("o")

    print_set(table)

    print("'no' in table?", table.contains("no"))
    table.remove("9")
    print("'9' in table?", table.contains("9"))

    print_set(table)
    print(table)
    print(repr(table))


def test2():
    """
    This test creates a table with less than minimum limit
    """
    table = LinkedHashSet(2, 0.75)
    table.remove("t")
    table.add("f")
    table.add("gt")
    table.add("p")
    table.remove("jh")
    table.remove("gt")
    table.add("t")
    table.add("gh")
    table.add("l")

    print_set(table)

    print("'z' in table?", table.contains("z"))
    table.remove("9")
    print("'gh' in table?", table.contains("gh"))

    print_set(table)
    print(table)
    print(repr(table))


def default_hash_func(value: Any = None, table_capacity: int = 10):
    return ord(value[0]) % table_capacity


def test3():
    """
    This method uses a bad default hash function
    """
    table = LinkedHashSet(6, 0.9, default_hash_func)
    table.remove("t")
    table.add("f")
    table.add("ft")
    table.add("p")
    table.remove("jh")
    table.remove("gt")
    table.add("t")
    table.add("gh")
    table.add("l")

    print_set(table)

    print("'u' in table?", table.contains("u"))
    table.remove("9")
    print("'hello' in table?", table.contains("hello"))

    print_set(table)
    print(table)
    print(repr(table))


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
