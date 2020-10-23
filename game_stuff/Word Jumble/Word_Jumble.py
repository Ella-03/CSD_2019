#!/usr/bin/python3
#Ella Adam
#11/4/19


'''Word Jumble - This game randomly selects a word from a word bank (list) and 
scrambles it. Then the user tries to guess the actual word'''
import random as rd

def welcome():
    print("""
                  Welcome To WORD JUMBLE
                =========================
            Try to guess these scrambled words""")
    
def jumbler(word):
    temp = list(word)
    rd.shuffle(temp)
    
    return ''.join(temp)

if __name__ == "__main__":
    word_bank = ["wing", "python", "computer", "airplane", "crown", "tractor"]
    guess = ''
    tries = 0
    jumble = ''
    word = ''
    wrong_guess = True
    welcome()
    word = word_bank[rd.randrange(len(word_bank))]
    jumble = jumbler(word)
    
    print()
    print("Here's the jumbled word:")
    print(jumble)
    print("---------")
   

    while wrong_guess:
        guess = input("Your guess: ")
        if guess == word:
           
            print("Congrats! You got it right in", tries, "tries!")
            wrong_guess = False
        else:
            print("Incorrect! That's not correct")
            tries += 1




