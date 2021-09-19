#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Sept 2021
# This program can solve for the area of a circle using the radius
#   radius given by user


import math


def main():
    # This program can solve for the area of a circle using the radius

    # input
    radius = int(input("Enter the radius of the circle (cm) : "))

    # process
    area = math.pi * radius ** 2

    # output
    print("")
    print("The area is {0} cm².".format(area))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
