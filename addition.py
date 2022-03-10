#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the sum of two inputted numbers


import constants


def main():
    # I calculate circumference

    # input
    first_number = int(input("Enter the first integer to add: "))
    second_number = int(input("Enter the second integer to add: "))

    # process
    sum = first_number + second_number

    # output
    print("\n{0} + {1} = {2}".format(first_number, second_number, sum))
    print("\nDone.")


if __name__ == "__main__":
    main()
