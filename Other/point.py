#!/usr/bin/python3
#Ella Adam
#11/5/19

'''point.py

program file that makes a cartesian graph point'''

class Point(object):
    
   # def __init__(self, x=0, y=0):
    #    self.x = 0
     #   self.y = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
if __name__ == "__main__":
    point1 = Point(5,6)
    point2 = Point(2,3)
    #point3 = Point()
    #print(point3)
    print(point1)
    print(point2)
   