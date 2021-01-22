#!/usr/bin/python3
#Ella Adam
#11/6/19

'''Critter Class for virtual pet game

*The critter has 3 attributes, fitness, happiness, and 
satiation(being well feed).
*The values range from 120 - down to 0.
*Death occurs when any attribute reaches 0 
*Playing, feeding, and exercising are all functions that raise the corresponding
attributes by a random value.

*The purpose of the game is to keep the critter alive as long as possible!

'''

from datetime import datetime
import random as rd

class Critter(object):
    
    def __init__(self, name):
        self.happiness = 120
        self.fitness = 120
        self.satiation = 120
        self.birthday = datetime.now()
        self.name = name
    
    
    
    def talk(self):
#        name = input("Hi, I'm a critter! What's my name? ")
        print("Hi, I'm a critter named " + self.name)
        print("I was born: " + str(self.birthday.date()))
        print("My happiness score: " + str(self.happiness))
        print("My 'full tummy' score: " + str(self.satiation))
        print("My fitness score: " + str(self.fitness))
        print()
#        return msg
    
    def play(self):
        self.happiness += rd.randint(1,15)
        print("YAYYYYY!")
        print()
        if self.happiness > 120:
            self.happiness = 120
        
    
    def food(self):
        self.satiation += rd.randint(1,15)
        print("YUMMY!")
        print()
        if self.satiation > 120:
            self.satiation = 120
        
        
    def exercise(self):
        self.fitness += rd.randint(1,15)
        print("WHEW!")
        print()
        if self.fitness > 120:
            self.fitness = 120
        
            
    def slow_death(self):
        '''Reduce each attibute by a random amount 1-5'''
        self.happiness -= rd.randint(1,5)
        self.fitness -= rd.randint(1,5)
        self.satiation -= rd.randint(1,5)




if __name__ == "__main__":
    test_critter = Critter("Fluffy!")
#    test_critter.happiness = 100
    test_critter.play()
    test_critter.slow_death()
#    test_critter.fitness = 100
#    test_critter.exercise()
#    test_critter.satiation = 100
#    test_critter.food()
    print(test_critter.talk())
#    print("Critter's happiness is:", test_critter.happiness)
#    print("Critter's satiation is:", test_critter.satiation)
#    print("Critter's exercise is:", test_critter.fitness)
    