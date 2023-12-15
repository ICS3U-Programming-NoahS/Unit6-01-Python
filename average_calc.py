#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Dec 14th, 2023
# This program generates 10 random numbers
# then finds and displays the average of those numbers
import constants
import random


def main():
    # Create empty list
    list_of_int = []

    # Initialize the sum
    sum = 0

    # Use a for loop to add and generate all of the random numbers
    for counter in range(0, constants.MAX_ARRAY_SIZE):
        list_of_int.append(random.randint(constants.MIN_NUM, constants.MAX_NUM))
        sum = sum + list_of_int[counter]
        print(
            "{} added to the list at position {}.".format(list_of_int[counter], counter)
        )

    # Find the average
    average = sum / constants.MAX_ARRAY_SIZE

    # Display the average
    print("The average is {}".format(average))


if __name__ == "__main__":
    main()
