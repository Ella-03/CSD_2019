#!/usr/bin/python3
#Ella Adam
#10/29/19

#Given an int n, return the absolute difference between n and 21,
#except return double the absolute difference if n is over 21.


def diff21(n):
  if n <= 21:
    
    return (21 - n)
    
  else:
    
    return 2*(n - 21)
