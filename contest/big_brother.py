#!/usr/bin/python3
#Ella Adam
#1/7/2020

import tkinter as tk
import pickle

#global variables
DEFAULT = ("Arial", 15)

#Contents in datafile.pickle
database = {'324-88-4571': ['Gwen', 'Stacy', '1965'], '489-32-1009': ['Dean', 'Winchester', '1978'], '489-45-9834': ['Sam', 'Winchester', '1982'], '111-00-1010': ['Samus', 'Aran', '1986']}

#Definitions

def raise_records():
    frame_records.tkraise()
    
def quit():
    exit()

def raise_lookup():
    frame_lookup.tkraise()
    
def raise_add():
    frame_add.tkraise()
    
#Classes

class Records(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        
class Lookup(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.lbl_SSN = tk.Label(self, font = DEFAULT, 
                                   text = "What is the SSN: ")
        self.lbl_SSN.grid(row = 0, column = 0)
        
        self.ent_SSN = tk.Entry(self, font = DEFAULT, show = '#')
        self.ent_SSN.grid(row = 0, column = 1)
        
        self.btn_search = tk.Button(self, text = "Submit", font = DEFAULT)
        self.btn_search.grid(row = 1, column = 0, columnspan = 1)

class Add(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        

    
 
# main window
root = tk.Tk()
#root.wm_geometry("260x230")
root.title("Big Brother Inc.")

#Creates Records frame
frame_records = Records()
frame_records.grid(row = 0, column = 0, sticky = "news")

#Creates Lookup frame
frame_lookup = Lookup()
frame_lookup.grid(row = 0, column = 0, sticky = "news")

#Creates Add frame
frame_add = Add()
frame_add.grid(row = 0, column = 0, sticky = "news")


#Question for user
lbl_question = tk.Label(text = "What would you like to do?",font = DEFAULT)
lbl_question.grid(row = 1, column = 0, columnspan = 1)

#Buttons for the user to choose
btn_records = tk.Button(text = "Print all records", font = DEFAULT, command = raise_records)
btn_records.grid(row = 2, column = 0, columnspan = 1)

btn_lookup = tk.Button(text = "Look up person by SSN", font = DEFAULT, command = raise_lookup)
btn_lookup.grid(row = 3, column = 0, columnspan = 1)

btn_add = tk.Button(text = "Add new person", font = DEFAULT, command = raise_add)
btn_add.grid(row = 4, column = 0, columnspan = 1)

btn_quit = tk.Button(text = "Quit", fon = DEFAULT, command = quit)
btn_quit.grid(row = 5, column = 0, columnspan = 1)




#End loop
frame_records.tkraise()
root.mainloop()