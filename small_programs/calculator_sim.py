# Program to simulate a basic calculator and it's functions
from tkinter import *

def button_press():
    pass

def equals():
    pass

def clear():
    pass

window = Tk()

window.title("Calculator Program")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("Chiller", 35), bg='white', width=24, height=2)
label.pack()

window.mainloop()