__author__ = 'MA'
"""
CSCI-603 Lab 6: AiRIT

A program to carry RIT students to their destination with a specific gate 
capacity and the aircraft capacity. It takes into account the name of the 
passenger, the ticket number and if the passenger has a carry-on bag or not.

Author: Mariam Abidi
"""
import sys
from cs_stack import Stack
from gate import Gate
from passenger import Passenger
from aircraft import Aircraft


def info_prompt() -> tuple[int, int]:
    """
    This method is to take input from the user about the gate capacity and the
    aircraft's capacity.
    :return: Returns the gate capacity value and aircraft capacity value
    """
    error_occurred = True
    while error_occurred:
        try:
            gate_capacity = int(input("Gate capacity: "))
            aircraft_capacity = int(input("Aircraft capacity: "))
            if gate_capacity > 0 and aircraft_capacity > 0:
                error_occurred = False
                return gate_capacity, aircraft_capacity
            else:
                # Error if any value is negative
                print("Error: Negative Integers Not Allowed!")
        # Error msg if the input value is not an integer
        except ValueError:
            print("Error: Only Positive Integers Allowed!")


def line_up(airit_gate: Gate, passenger: list, ticket_no: str) -> Gate:
    """
    A method to line up a passenger on the respective boarding zone according
    to their ticket number.
    :param airit_gate: A variable to for the gate class object.
    :param passenger: A variable to store the information of the passenger
    :param ticket_no: A variable to store the ticket number of the passenger
    :return: Returns the Gate with updated passenger inside
    """
    new_passenger = Passenger(passenger[0], passenger[1], passenger[2])
    airit_gate.add_passenger(type[int(ticket_no[0])], new_passenger)
    return airit_gate


def line_up_counter\
                (passenger_list: list, gate_capacity: int,
                 aircraft_capacity: int, flights=0) -> int:
    """
    A method to line up the passengers on the gate and board the passengers
    accordingly.
    :param passenger_list: A variable to store the complete passenger list
    :param gate_capacity: A variable to store the gate's capacity
    :param aircraft_capacity: A variable to store the aircraft's capacity
    :param flights: A variable to store the number of flights
    :return: Returns the number of flights
    """
    while len(passenger_list) > 0:
        print("Passengers are lining up at the gate...")
        gate_capacity_counter = 0
        list_count = 0
        airit_gate = Gate()
        while (gate_capacity_counter < gate_capacity
               and list_count < len(passenger_list)):
            passenger = passenger_list[list_count]
            print("\t" + str(passenger[0]) + ", ticket: " +
                  str(passenger[1]) + ", carry_on: " + str(passenger[2]))
            line_up(airit_gate, passenger, passenger[1])
            passenger_list.remove(passenger)
            gate_capacity_counter += 1
        if gate_capacity_counter == gate_capacity:
            print("The gate is full; remaining passengers must wait.")
        else:
            print("The last passenger is in line!")
        flights += boarding_aircraft(airit_gate, aircraft_capacity)
        if len(passenger_list) == 0:
            return flights
        else:
            return line_up_counter(passenger_list, gate_capacity,
                                   aircraft_capacity, flights)


def boarding_aircraft(passengers_at_gate: Gate, aircraft_capacity: int):
    """
    A method to board the passengers on the flight.
    :param passengers_at_gate: A variable to store passengers at gate
    :param aircraft_capacity: A variable to store the gate capacity
    :return: Returns the number of flights
    """
    with_carry_on_stack = Stack()
    without_carry_on_stack = Stack()
    rit_aircraft = Aircraft(with_carry_on_stack, without_carry_on_stack)
    aircraft_capacity_counter = 0
    flights = 0
    while passengers_at_gate.gate_is_empty() is False:
        print("Passengers are boarding the aircraft...")

        # Boarding the passengers from boarding zone 4 first
        while (passengers_at_gate.zone_is_empty(4) is False
               and aircraft_capacity_counter < aircraft_capacity):
            passenger_boarding = passengers_at_gate.peek_passenger(4)
            rit_aircraft.enter(passenger_boarding, passenger_boarding.carryOn)
            print(
                "\t" + passenger_boarding.name + ", ticket: "
                + passenger_boarding.ticketNo + ", carry_on: " +
                passenger_boarding.carryOn)
            passengers_at_gate.remove_passenger(4, )
            aircraft_capacity_counter += 1

        # Boarding the passengers from boarding zone 3 second
        while (passengers_at_gate.zone_is_empty(3) is False
               and aircraft_capacity_counter < aircraft_capacity):
            passenger_boarding = passengers_at_gate.peek_passenger(3)
            rit_aircraft.enter(passenger_boarding, passenger_boarding.carryOn)
            print(
                "\t" + passenger_boarding.name + ", ticket: "
                + passenger_boarding.ticketNo + ", carry_on: " +
                passenger_boarding.carryOn)
            passengers_at_gate.remove_passenger(3)
            aircraft_capacity_counter += 1

        # Boarding the passengers from boarding zone 2 third
        while (passengers_at_gate.zone_is_empty(2) is False
               and aircraft_capacity_counter < aircraft_capacity):
            passenger_boarding = passengers_at_gate.peek_passenger(2)
            rit_aircraft.enter(passenger_boarding, passenger_boarding.carryOn)
            print(
                "\t" + passenger_boarding.name + ", ticket: "
                + passenger_boarding.ticketNo + ", carry_on: " +
                passenger_boarding.carryOn)
            passengers_at_gate.remove_passenger(2)
            aircraft_capacity_counter += 1

        # Boarding the passengers from boarding zone 1 last
        while (passengers_at_gate.zone_is_empty(1) is False
               and aircraft_capacity_counter < aircraft_capacity):
            passenger_boarding = passengers_at_gate.peek_passenger(1)
            rit_aircraft.enter(passenger_boarding, passenger_boarding.carryOn)
            print(
                "\t" + passenger_boarding.name + ", ticket: "
                + passenger_boarding.ticketNo + ", carry_on: " +
                passenger_boarding.carryOn)
            passengers_at_gate.remove_passenger(1)
            aircraft_capacity_counter += 1

        if aircraft_capacity_counter == aircraft_capacity:
            flights += 1
            print("The aircraft is full.")
            print("Ready for taking off ...")
            print("The aircraft has landed.")
            disembarking(rit_aircraft)
            aircraft_capacity_counter = 0
            if passengers_at_gate.gate_is_empty():
                return flights
        elif (passengers_at_gate.gate_is_empty()
              and aircraft_capacity_counter < aircraft_capacity):
            flights += 1
            print("There are no more passengers at the gate.")
            print("Ready for taking off ...")
            print("The aircraft has landed.")
            disembarking(rit_aircraft)
            return flights


def disembarking(rit_aircraft: Aircraft):
    """
    A method to disembark the passengers from the aircraft.
    :param rit_aircraft: A variable to store the aircraft object
    """
    print("Passengers are disembarking...")
    while rit_aircraft.without_carry_on.is_empty() is False:
        passenger_on_top = rit_aircraft.without_carry_on.peek()
        print("\t" +
              passenger_on_top.name + ", ticket: "
              + passenger_on_top.ticketNo + ", carry_on: " +
              passenger_on_top.carryOn)
        rit_aircraft.without_carry_on.pop()
    while rit_aircraft.with_carry_on.is_empty() is False:
        passenger_on_top = rit_aircraft.with_carry_on.peek()
        print("\t" +
              passenger_on_top.name + ", ticket: "
              + passenger_on_top.ticketNo + ", carry_on: " +
              passenger_on_top.carryOn)
        rit_aircraft.with_carry_on.pop()


def user_input():
    """
    A method to take the command line arguments and the read the file specified
    :return: None
    """
    passenger_list = list()
    passengers = 0
    length_of_args = len(sys.argv)
    if length_of_args < 2:
        print("Usage: python3 airit.py {filename}")
    elif length_of_args == 2:
        path = "../data/"
        filename = sys.argv[1]
        try:
            with open(path + filename) as f:
                gate_capacity, aircraft_capacity = info_prompt()
                print("Reading passenger data from " + filename)
                for line in f:
                    passenger = line.strip().split(',')
                    passengers += 1
                    passenger_list.append(passenger)
                print("Beginning simulation...")
                flights = line_up_counter(passenger_list,
                                          gate_capacity, aircraft_capacity)
                print("Simulation complete. Statistics: "
                      + str(flights) + " flights, " + str(passengers) +
                      " passengers are at their destination.")

        except FileNotFoundError:
            print("File not found: {" + filename + "}")


def main() -> None:
    """
    The main loop responsible for getting the input details from the user
    and running the AiRIT's simulation.
    :return: None
    """
    user_input()


# Main Conditional Guard
if __name__ == '__main__':
    main()
