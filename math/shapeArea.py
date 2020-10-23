#!/usr/bin/python3
#Ella Adam
#9/5/2019

'''This program computes the area of a retangle, circle, or a triangle'''
print("  Welcome to the Area Program!\n\n")

# Have the user choose which area to calculate
usersChoice = inp

# length <- input
length = input("Input length: ")
length = float(length)

#width <- input
width = input("Input width: ")
width = float(width)

# area <- length * width
area = length * width

# display area
print("Area is:", area)
