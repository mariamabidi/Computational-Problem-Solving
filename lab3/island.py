__author__ = 'MA'

"""
CSCI-603 Lab 3: Islands

A program that uses recursive calls to draw islands based on user's input of
the number of sides, side length and levels. It prints the total perimeter of
the island. Firstly, the island is made with the curve 1 and then draws the
island with same dimensions for curve 2.
The user's input should be an integer value.

pre: pos (0,0), heading (east), down.
post: pos (0,0), heading (east), down.

Author: Mariam Abidi
"""

import turtle as t
import math
import time
import re

t.setup(1000, 1000)


def side_curve_1(n, l):
    """
    This function is used to draw the island using the first curve.

    :param n: A variable to store the side length.
    :param l: A variable to store the level.
    :return: Returns the accumulated length value, acc
    """
    acc = 0
    if l == 1:  # Base Case
        t.forward(n)
        acc += n
    elif l == 2:  # First Recursive Step
        t.forward(n / 3)
        acc += n / 3
        t.left(60)
        acc += side_curve_1((n / 3), l - 1)
        t.right(120)
        acc += side_curve_1((n / 3), l - 1)
        t.left(60)
        t.forward(n / 3)
        acc += n / 3
    elif l > 2:  # Second Recursive Step
        acc += side_curve_1((n / 3), l - 1)
        t.left(60)
        acc += side_curve_1((n / 3), l - 1)
        t.right(120)
        acc += side_curve_1((n / 3), l - 1)
        t.left(60)
        acc += side_curve_1((n / 3), l - 1)
    return acc  # Accumulated Length Value


def side_curve_2(n, l):
    """
    This function is used to draw the island using the second curve.

    :param n: A variable to store the side length.
    :param l: A variable to store the level.
    :return: Returns the accumulated length value, acc
    """
    acc = 0
    if l == 1:  # Base Case
        t.forward(n)
        acc += n
    else:  # Recursive Step
        t.left(45)
        acc += side_curve_2(n / math.sqrt(2), l - 1)
        t.right(90)
        acc += side_curve_2(n / math.sqrt(2), l - 1)
        t.left(45)
    return acc  # Accumulated Length Value


def side_error_check():
    """
    This function is used to check if the user input for the number of sides is
    an integer or not.

    :return: Returns the side value if it is an integer else throws error and
    returns input field again.
    """
    side = input("Number of island's sides = ")
    pattern = '^[-+]?[0-9]+$'

    # Checks if the input matches the pattern.
    if re.fullmatch(pattern, side):
        return side

    # Checks if the input is a string value
    elif re.fullmatch(r'.*', side):
        print("Value must be an integer, you entered a 'string-value'.")
        return side_error_check()
    else:
        print("Invalid type.")
        return side_error_check()


def side_length_error_check():
    """
    This function is used to check if the user input for the side length is
    an integer or not.

    :return: Returns the side length value if it is an integer else throws
    error and returns input field again.
    """
    side_length = input("Number of side length = ")
    float_pattern = '^[-+]?[0-9]+.[0-9]*$'

    # Checks if the input matches the pattern.
    if re.fullmatch(float_pattern, side_length):
        return side_length

    # Checks if the input is a string value
    elif re.fullmatch(r'.*', side_length):
        print("Value must be an integer, you entered a 'string-value'.")
        return side_length_error_check()
    else:
        print("Invalid type.")
        return side_length_error_check()


def level_error_check():
    """
    This function is used to check if the user input for the number of levels
    is an integer or not.

    :return: Returns the side value if it is an integer else throws error and
    returns input field again.
    """
    level = input("Number of levels = ")
    pattern = '^[-+]?[0-9]+$'

    # Checks if the input matches the pattern.
    if re.fullmatch(pattern, level):
        return level

    # Checks if the input is a string value
    elif re.fullmatch(r'.*', level):
        print("Value must be an integer, you entered a 'string-value'.")
        return level_error_check()
    else:
        print("Invalid type.")
        return level_error_check()


def main():
    """
    This is the main function that takes all the user inputs for the number of
    sides, side length and the number of levels and prints the island with
    curve 1 and curve 2 accordingly.

    :return: None
    """
    # Stores the final number of sides
    final_side = side_error_check()

    # Stores the final side length.
    final_side_length = side_length_error_check()

    # Stores the final number of levels
    final_level = level_error_check()

    # Calculates the angle between two sides.
    angles = 360 / int(final_side)

    # Variable to store the perimeter of first curve.
    end_length_1 = 0

    # Variable to store the perimeter of second curve.
    end_length_2 = 0

    # Checks if the user input is a positive integer.
    if (int(final_side) > 0 and float(final_side_length) > 0
            and int(final_level) > 0):
        t.tracer(0, 0)

        # For loop to draw the island with first curve with the total number
        # of sides.
        for _ in range(int(final_side)):
            end_length_1 \
                += side_curve_1(float(final_side_length), int(final_level))
            t.right(360 - angles)

        # Prints the total perimeter.
        print(end_length_1)
        t.update()
        input('PRESS ENTER')
        time.sleep(int())
        t.reset()
        t.tracer(0, 0)

        # For loop to draw the island with second curve with the total number
        # of sides.
        for _ in range(int(final_side)):
            end_length_2 \
                += side_curve_2(float(final_side_length), int(final_level))
            t.right(360 - angles)

        # Prints the total perimeter.
        print(end_length_2)
        print("ByeByee!!!!")
        t.update()
    else:
        print("Invalid Value")

    t.mainloop()


# Main Conditional Guard
if __name__ == '__main__':
    main()