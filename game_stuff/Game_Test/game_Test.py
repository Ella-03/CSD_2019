#!/usr/bin/python3
#Ella Adam
#10/30/19

'''Program to test basic function of an adventure game'''
#from dieroller import d20
import dieroller as dr

def attack(defense):    
    
    '''defense = integer defense value, returns boolean!"'''
    
    '''takes a defense value as a perameter and computes a d20 roll, if the roll
    meets of exceeds the defense valus, return "True" else return "False" '''
    
    roll = dr.d20()
    if roll >= defense:
        return "True"
    else:
        return "False"
    print("I don't think you should have drunk the hemlock...")
    if is_poisoned(8):
        print("On the bright side, you get the same death as Socrates")
    else:
        print("HUH! Looks like no death for YOU!")
    
def is_poisoned(con_mod):
    '''con_mod = integer value, returns boolean 
    On a d20 roll: 1-10 ---> Poisoned  11-20 --> Not Poisoned
    The con_mod is added to the roll to swing the distribtion up or down'''
    roll = d20
    if roll + con_mod <= 10:
        return "True"
    else:
        return "False"
    
if __name__ =="__main__":
    if attack(10):
        print("You HIT!")
    else:
        print("Whiff! Lame!")