#!/usr/bin/python3
# big_brother.py
# Thorin Schmidt
# 1/7/2020

import pickle

'''Runs prototype as specified in Contest_Instructions.txt'''

def print_all(sort_it):
    #print("running print_all()")
    key_list = people.keys()
    if sort_it:
        sorted_list =[]
        for key in key_list:
            sorted_list.append(key)
        sorted_list.sort()
        key_list = sorted_list
        
    for key in key_list:
        print()
        print("SSN: ", key)
        print("Name: ", people[key][1]+", "+people[key][0])
        print("Birth Year: ", people[key][2])
        print("----------------------")

def lookup():
    ssn = input("What is the SSN? ")
    if ssn in people:
        print()
        print("SSN: ", ssn)
        print("Name: ", people[ssn][1]+", "+people[ssn][0])
        print("Birth Year: ", people[ssn][2])
        print("----------------------")
    else:
        print("*** NUMBER NOT FOUND! ***\n")

def lookup_by_name():
    found_one = False
    name = input("  What is the last name of the person? ")
    for key in people.keys():
        if name == people[key][1]:
            found_one = True
            print()
            print("SSN: ", key)
            print("Name: ", people[key][1]+", "+people[key][0])
            print("Birth Year: ", people[key][2])
            print("----------------------")
            
    if not found_one:
        print("*** NO MATCHES FOUND!***\n")

def add_new():
    #print("running add_new()")
    ssn = input("What is the SSN of the person to add? ")
    if ssn in people:
        print("*** THAT SSN ALREADY EXISTS! ***\n")
    else:
        first = input("   What is their first name? ")
        last = input("   What is their last name? ")
        year = input("   What is their birth year? ")
        people[ssn] = [first, last, year]
        
def edit_record():
    ssn = input("What is the SSN of the person to edit? ")
    if ssn not in people:
        print("*** THAT SSN DOES NOT EXIST! ***\n")
    else:
        first = input("   What is their first name? ")
        last = input("   What is their last name? ")
        year = input("   What is their birth year? ")
        people[ssn] = [first, last, year]  
        
def delete_record():
    ssn = input("What is the SSN of the person to delete? ")
    if ssn not in people:
        print("*** THAT SSN DOES NOT EXIST! ***\n")
    else:
        entry = people.pop(ssn)
        print(ssn, ":", entry[0], entry[1]+", removed.")

def quit():
    #print("running quit()")
    pickle_file = open("datafile.pickle", "wb")
    pickle.dump(people, pickle_file)
    pickle_file.close()
    

people = {}
pickle_file = open("datafile.pickle", "rb")
people = pickle.load(pickle_file)
pickle_file.close()


keep_going = True

while keep_going:
    print("""
    Welcome to Big Brother Inc.
    ---------------------------
    
    MAIN MENU
    1) Print All Records
    2) Look Up Person by SSN
    3) Add New Person
    
    4) Print All Records Sorted by SSN
    5) Edit Existing Person
    6) Delete Person from Database
    7) Look Up Person by Name
    
    Q) Quit
    
    """)
    
    choice = input("What would you like to do? ")
    if choice == "1":
        print_all(False)
    elif choice == "2":
        lookup()
    elif choice == "3":
        add_new()
    elif choice == "4":
        print_all(True)
    elif choice == "5":
        edit_record()
    elif choice == "6":
        delete_record()
    elif choice == "7":
        lookup_by_name()
    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False
    else:
        print("*** NOT A VALID CHOICE ***\n")
        
print("Goodbye.") 
        
