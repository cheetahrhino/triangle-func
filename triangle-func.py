# Program to compute the area of a triangle give the length of its three sides

from math import *

def triArea(a, b, c):

    s = (a + b + c) / 2

    # area = sqrt(s * (s-a) * (s-b) * (s-c))

    x = s - a
    y = s - b
    z = s - c


    area = sqrt(s * x * y * z)

    return area


def main():
    print("This program calculates the area of triangle given all the 3 sides.")
    print()

    s1 = float(input("Enter the length of the first side: "))
    s2 = float(input("Enter the length of the second side: "))
    s3 = float(input("Enter the length of the third side: "))

    area = triArea(s1, s2, s3)

    print("The area of a triangle with side {0:0.3f}, {1:0.3f} and {2:0.3f} is {3:0.5f}".format(s1,s2,s3,area))

main()