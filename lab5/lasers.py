__author__ = 'MA'

"""
CSCI-603 Lab 5: Lasers

A program to solve a rectangular puzzle using command line arguments. It 
provides users with the desired number of optimal lasers.

Author: Mariam Abidi
"""
import sys
from dataclasses import dataclass
import quick_sort


@dataclass
class Laser:
    center: int
    coordinates: tuple
    facing: str
    total_sum: int


def laser_placement(puzzle_list: list):
    """
    This function is used to place all the possible lasers and create a list of
    all the lasers present.
    :param puzzle_list: A variable to store the list containing the puzzle
    :return: Returns the sorted list of lasers
    """
    puzzle = list()

    # A for loop to separate all the elements
    for element in puzzle_list:
        element_list = element.split()
        puzzle.append(element_list)
    lasers_list = list()

    # A double for loop to create all the possible lasers
    for row_count, rows in enumerate(puzzle):
        for column_count, columns in enumerate(rows):

            # Eliminates all the corner values
            if ((row_count == 0 and column_count == 0)
                    or (row_count == 0 and column_count == len(rows) - 1)
                    or (row_count == len(puzzle) - 1 and column_count == 0)
                    or (row_count == len(puzzle) - 1
                        and column_count == len(rows) - 1)):
                continue

            # Condition for all the possible value that can have
            # north facing lasers
            if (row_count != 0 and column_count != 0
                    and column_count != len(rows) - 1):
                previous_row = puzzle[row_count - 1]
                center_column = rows.index(columns)
                previous_number = rows[column_count - 1]
                next_number = rows[column_count + 1]
                above_number = previous_row[center_column]
                lasers_list.append(Laser(
                    center=columns,
                    coordinates=(row_count, column_count),
                    facing="N",
                    total_sum=(int(previous_number) + int(next_number)
                               + int(above_number))
                ))

            # Condition for all the possible value that can have
            # south facing lasers
            if (row_count != len(puzzle) - 1 and column_count != 0
                    and column_count != len(rows) - 1):
                next_row = puzzle[row_count + 1]
                center_column = column_count
                previous_number = rows[column_count - 1]
                next_number = rows[column_count + 1]
                below_number = next_row[center_column]
                lasers_list.append(Laser(
                    center=columns,
                    coordinates=(row_count, column_count),
                    facing="S",
                    total_sum=(int(previous_number) + int(next_number)
                               + int(below_number))
                ))

            # Condition for all the possible value that can have
            # east facing lasers
            if (row_count != 0 and row_count != len(puzzle) - 1
                    and column_count != len(rows) - 1):
                previous_row = puzzle[row_count - 1]
                next_row = puzzle[row_count + 1]
                center_column = column_count
                above_number = previous_row[center_column]
                below_number = next_row[center_column]
                right_side_number = rows[center_column + 1]
                lasers_list.append(Laser(
                    center=columns,
                    coordinates=(row_count, column_count),
                    facing="E",
                    total_sum=(int(above_number) + int(below_number)
                               + int(right_side_number))
                ))

            # Condition for all the possible value that can have
            # west facing lasers
            if (row_count != 0 and row_count != len(puzzle) - 1
                    and column_count != 0):
                previous_row = puzzle[row_count - 1]
                next_row = puzzle[row_count + 1]
                center_column = column_count
                above_number = previous_row[center_column]
                below_number = next_row[center_column]
                left_side_number = rows[center_column - 1]
                lasers_list.append(Laser(
                    center=columns,
                    coordinates=(row_count, column_count),
                    facing="W",
                    total_sum=(int(above_number) + int(below_number)
                               + int(left_side_number))
                ))

    return quick_sort.quick_sort_list(lasers_list)


def read_file(filename: str):
    """
    This function is used to read a file.
    :param filename: A variable to store the filename
    :return: Returns a sorted list of all possible lasers.
    """
    puzzle_list = list()
    with open(filename) as f:
        for lines in f:
            puzzle_list.append(lines.strip())
        for lines in puzzle_list:
            print(lines, end='\n')
    return laser_placement(puzzle_list)


def user_input():
    """
    This method controls all the user input functionality.
    """
    length_of_args = len(sys.argv)
    if length_of_args == 2:
        print("Loaded: " + sys.argv[1])
        laser_list = read_file(sys.argv[1])
        user_choice = int(input("Enter number of lasers: "))
        total_sum = 0
        m = 0
        n = 0
        new_dict = dict()
        key_list = list()
        if user_choice > len(laser_list):
            print("Too many lasers to place!")
        else:
            if user_choice == 0 and len(laser_list) == 0:
                print("Total Sum: " + str(total_sum))
            else:
                # A loop to remove lasers having the same coordinates.
                while n < len(laser_list):
                    if laser_list[n].coordinates not in new_dict:
                        key_list.append(laser_list[n].coordinates)
                        new_dict[laser_list[n].coordinates] = laser_list[n]
                        n += 1
                    else:
                        n += 1
                        continue

                if user_choice > len(new_dict):
                    print("Too many lasers to place!")
                elif user_choice == 0:
                    print("Total Sum: " + str(total_sum))
                else:
                    # Printing all the optimal placements
                    print("Optimal Placements: ")
                    while m < user_choice:
                        print("loc: " +
                              str(new_dict[key_list[m]].coordinates) +
                              ", facing: "
                              + str(new_dict[key_list[m]].facing) + ", sum: "
                              + str(new_dict[key_list[m]].total_sum))
                        total_sum += int(new_dict[key_list[m]].total_sum)
                        m += 1
                    print("Total Sum: " + str(total_sum))

    else:
        print("Usage: python3 lasers.py filename")


def main():
    """
    The main program.
    """
    user_input()


# Main Conditional Guard
if __name__ == '__main__':
    main()
