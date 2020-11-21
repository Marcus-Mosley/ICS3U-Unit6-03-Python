#!/usr/bin/env python3
#
# Created by Marcus A. Mosley
# Created on November 2020
# This program finds the smallest number of a random array of 10 numbers

import random


def max_number(number_array):
    # This function finds the smallest number of a random array of 10 numbers

    smallest_number = 101

    for loop_counter in number_array:
        if loop_counter < smallest_number:
            smallest_number = loop_counter

    return smallest_number


def main():
    # This function receives input

    number_array = []

    # Input
    for loop_counter in range(0, 10):
        number = random.randint(1, 100)
        number_array.append(number)
        print("The random number is: {}".format(number))
    print(" ")

    # Call Functions
    smallest_number = max_number(number_array)

    print("The smallest number is {}".format(smallest_number))


if __name__ == "__main__":
    main()
