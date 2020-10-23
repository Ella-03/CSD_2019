#!/usr/bin/python3
#Ella Adam
#9/23/19

def simple_message():
  print("Hi, Have a good day!")

def translated_message(language):
  if language == "english":
    print("Have a good day!")
  elif language == "spanish":
    print("Tenga un buen dia")
  elif language == "french":
    print("Bonne journee")
  elif language == "portugese":
    print("Tenha um bom dia")
  else:
    print("Sorry, I don't speak", language)
  
  
# call on the functions
simple_message()
translated_message("french")
  
