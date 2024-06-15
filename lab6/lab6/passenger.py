__author__ = 'MA'
"""
CSCI-603 Lab 6: AiRIT

A program to carry RIT students to their destination with a specific gate 
capacity and the aircraft capacity. It takes into account the name of the 
passenger, the ticket number and if the passenger has a carry-on bag or not.

Author: Mariam Abidi
"""


class Passenger:
    """
    A class to create the passenger's structure.
    """
    __slots__ = "name", "ticketNo", "carryOn"
    _name = str
    _ticketNo = str
    _carryOn = bool

    def __init__(self, _name=str, _ticketNo=str, _carryOn=bool):
        self.name = _name
        self.ticketNo = _ticketNo
        self.carryOn = _carryOn

    def __str__(self) -> str:
        return "[" + str(self.name) + "," + str(self.ticketNo) + "," + str(self.carryOn) + "]"
