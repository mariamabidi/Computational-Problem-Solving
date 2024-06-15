__author__ = 'MA'
"""
CSCI-603 Lab 6: AiRIT

A program to carry RIT students to their destination with a specific gate 
capacity and the aircraft capacity. It takes into account the name of the 
passenger, the ticket number and if the passenger has a carry-on bag or not.

Author: Mariam Abidi
"""
from typing import Any
from cs_stack import Stack


class Aircraft():
    """
    A class to create the aircraft structure.
    """
    __slots__ = "with_carry_on", "without_carry_on"
    _with_carry_on = Stack()
    _without_carry_on = Stack()

    def __init__(self, with_carry_on: Stack(), without_carry_on: Stack()):
        self.with_carry_on = with_carry_on
        self.without_carry_on = without_carry_on

    def enter(self, newValue: Any, carryOn: str):
        """
        A method to enter a passenger inside the aircraft
        :param newValue: A variable to store the passenger
        :param carryOn: A variable to store the carryOn information
        :return: None
        """
        if carryOn == "False":
            self.without_carry_on.push(newValue)
        else:
            self.with_carry_on.push(newValue)

    def exit(self):
        """
        A method to remove a passenger from the aircraft
        :return: None
        """
        while self.without_carry_on is not None:
            self.without_carry_on.pop()
        while self.with_carry_on is not None:
            self.with_carry_on.pop()

    def __str__(self):
        return "[" + self.with_carry_on + self.without_carry_on + "]"
