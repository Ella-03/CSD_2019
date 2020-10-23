#!/usr/bin/python3
#Name: Ella Adam
#Date: 9/4/19
'''This program will compute the area of a triangle after being given the length of a base and height by the user'''

print("Triangle Area")
print("-------------")
print()

# length of base <- input
length = input("Input length of base: ")
length = float(length)

# height <- input
height = input("Input height: ")
height = float(height)

# area <- length of (base *  height)/2
area = (length * height)/2

#display area
print("The area of the triangle is:", area)
