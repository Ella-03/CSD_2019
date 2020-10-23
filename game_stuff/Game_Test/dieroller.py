#!/usr/bin/python3
# Thorin Schmidt
# 9/24/2019

''' Create a die rolling module to demonstrate abstraction '''

import random as rd

def d4():
    return rd.randint(1,4)

def d6():
    return rd.randint(1,6)

def d8():
    return rd.randint(1,8)

def d10():
    return rd.randint(1,10)

def d12():
    return rd.randint(1,12)

def d20():
    return rd.randint(1,20)

def d100():
    return rd.randint(1,100)

def dice_rolls(times, die):
    result = []
    for i in range(times):
        if die == 4:
            result.append(d4())
        elif die == 6:
            result.append(d6())
        elif die == 8:
            result.append(d8())
        elif die == 10:
            result.append(d10())
        elif die == 12:
            result.append(d12())
        elif die == 20:
            result.append(d20())
        elif die == 100:
            result.append(d100())
    return result


def total_dice_rolls(times, die):
    ''' rolls dice then totals them'''
    
    dice_pool = dice_rolls(times, die)
    total = 0
    
    for die in dice_pool:
        total += die
    
    return total

#Main Section
#if __name__ == "__main__":
for i in range(50):
    print("rolling d4:  ", d4())
print()

for i in range(20):
    print("rolling d6:  ", d6())
print()
    
for i in range(20):        
    print("rolling d8:  ", d8())
print()

for i in range(20):    
    print("rolling d10: ", d10())
print()

for i in range(20):    
    print("rolling d12: ", d12())
print()

for i in range(20):    
    print("rolling d20: ", d20())
print()
    
for i in range(20):    
    print("rolling d100:", d100())
print()
    
rolls = dice_rolls(5, 20)
print("rolling 5d20: ", rolls)
print()

total_roll = total_dice_rolls(5,20)
print("rolling 5d20 total: ", total_roll)