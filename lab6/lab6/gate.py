__author__ = 'MA'
"""
CSCI-603 Lab 6: AiRIT

A program to carry RIT students to their destination with a specific gate 
capacity and the aircraft capacity. It takes into account the name of the 
passenger, the ticket number and if the passenger has a carry-on bag or not.

Author: Mariam Abidi
"""
from passenger import Passenger
from cs_queue import Queue


class Gate:
    """
    A class to create the Gate structure.
    """
    __slots__ = "boarding_zone_list"
    _boarding_zone_list = []

    def __init__(self):
        for i in range(1, 5):
            self._boarding_zone_list.append(Queue("Boarding Zone " + str(i)))

    def add_passenger(self, boarding_zone=int, passenger=Passenger()):
        """
        A method to add passenger inside the respective boarding zone
        :param boarding_zone: A variable to store the boarding zone value
        :param passenger: A variable to store the passenger
        :return:
        """
        if boarding_zone == type[1]:
            first_zone = self._boarding_zone_list[0]
            first_zone.enqueue(passenger)
        elif boarding_zone == type[2]:
            second_zone = self._boarding_zone_list[1]
            second_zone.enqueue(passenger)
        elif boarding_zone == type[3]:
            third_zone = self._boarding_zone_list[2]
            third_zone.enqueue(passenger)
        elif boarding_zone == type[4]:
            fourth_zone = self._boarding_zone_list[3]
            fourth_zone.enqueue(passenger)

    def remove_passenger(self, boarding_zone=int):
        """
        A method to remove a passenger from the respective boarding zone
        :param boarding_zone: A variable to store the boarding zone value
        :return:
        """
        if boarding_zone == 1:
            first_zone = self._boarding_zone_list[0]
            first_zone.dequeue()
        elif boarding_zone == 2:
            second_zone = self._boarding_zone_list[1]
            second_zone.dequeue()
        elif boarding_zone == 3:
            third_zone = self._boarding_zone_list[2]
            third_zone.dequeue()
        elif boarding_zone == 4:
            fourth_zone = self._boarding_zone_list[3]
            fourth_zone.dequeue()

    def peek_passenger(self, boarding_zone=int):
        """
        A method to peek the passenger at front of the specified boarding zone
        :param boarding_zone: A variable to store the boarding zone value
        :return: None
        """
        passengers_in_queue = self._boarding_zone_list[boarding_zone - 1]
        if passengers_in_queue.is_empty() is False:
            passenger_in_front = passengers_in_queue.peek()
            return passenger_in_front

    def zone_is_empty(self, boarding_zone: int):
        """
        A method to check if a zone is empty or not.
        :param boarding_zone: A variable to store the boarding zone value
        :return: None
        """
        return self._boarding_zone_list[boarding_zone - 1].is_empty()

    def gate_is_empty(self):
        """
        A method to check if the gate is empty or not.
        :return:
        """
        return (self._boarding_zone_list[0].is_empty() and
                self._boarding_zone_list[1].is_empty() and
                self._boarding_zone_list[2].is_empty() and
                self._boarding_zone_list[3].is_empty())

    def __str__(self):
        return ("[" + str(self._boarding_zone_list[0].name) + " "
                + str(self._boarding_zone_list[0]) +
                ", " + str(self._boarding_zone_list[1].name) + " "
                + str(self._boarding_zone_list[1]) +
                ", " + str(self._boarding_zone_list[2].name) + " "
                + str(self._boarding_zone_list[2]) +
                ", " + str(self._boarding_zone_list[3].name) + " "
                + str(self._boarding_zone_list[3]) + "]")
