#!/usr/bin/python3
#Ella and Logan
#10/31/19


'''Program Allows User To Input 5 Student Names And Marks To Print A Report (loop)'''

students=[]
for num in range(5):
    x=input("Enter name of students: ")
    students.append(x)

marks=[]
for num in range(5):
    y=input("Enter marks of students:")
    marks.append(y)

report = input("Do you want to print class report?: ")
if report == 'yes':
    print(x[0],":", y[0])
    print(x[1],":", y[1])
    print(x[2],":", y[2])
    print(x[3],":", y[3])
    print(x[4],":", y[4])