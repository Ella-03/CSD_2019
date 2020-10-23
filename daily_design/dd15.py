#!/usr/bin/python3
#Ella Adam
#12/05/19

phonebook = {'James':'555-1234', 'Courtney':'555-4398', 'Alvin':'555-9276', 'Kim':'555-7859'}

lookup = input("What is the name?: ")

if lookup in phonebook.keys():
    print(phonebook[lookup])
else:
    print(lookup, ": " "Name not found")