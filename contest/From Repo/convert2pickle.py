#!/usr/bin/python3
# convert2pickle.py
# Thorin Schmidt
# 1/6/2020

import pickle

'''converts text file of datafile.txt into datafile.pickle'''

people = {}

text_file = open("datafile.txt", "r")
dalist = text_file.readlines()
#print(dalist)
for i in range(0, len(dalist), 4):
    key = dalist[i].strip()
    first = dalist[i+1].strip()
    last = dalist[i+2].strip()
    year = dalist[i+3].strip()
    people[key] = [first, last, year]

#print(people)

pickle_file = open("datafile.pickle", "wb")
pickle.dump(people, pickle_file)
pickle_file.close()
print("DONE...")

pickle_file = open("datafile.pickle", "wb")
pickle.dump(people, pickle_file)

pickle_file = open("datafile.pickle", "rb")
people2 = pickle.load(pickle_file)
print(people == people2)
pickle_file.close()
print("Winchester" in people2)