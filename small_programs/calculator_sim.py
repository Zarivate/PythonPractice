# Program to simulate a basic calculator and it's functions
from tkinter import *

def button_press(value):

    global equation_text

    equation_text = equation_text + str(value)

    equation_label.set(equation_text)

def equals():

    global equation_text

    # Try catch block for any divide by 0 shenanigans
    try:
        total = str(eval(equation_text))

        equation_label.set(total)

        # So can be reusable
        equation_text = total

    except ZeroDivisionError:
        equation_label.set("Invalid arithmetic")

        # Reset the equation text after
        equation_text = ""

    except SyntaxError:
        equation_label.set("Invalid syntax")

        # Reset the equation text after
        equation_text = ""
def clear():
    global equation_text

    equation_label.set("")

    equation_text = ""

window = Tk()

window.title("Calculator Program")
window.geometry("600x600")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("Comic Sans", 20), bg='white', width=24, height=2)
label.pack()

# All the buttons go down here
frame = Frame(window)
frame.pack()

# Will be using a grid for the buttons in order to get them placed correctly
button_1 = Button(frame, text=1, height=4, width=9, font=35, command= lambda: button_press(1))
button_1.grid(row=0, column=0)

button_2 = Button(frame, text=2, height=4, width=9, font=35, command= lambda: button_press(2))
button_2.grid(row=0, column=1)

button_3 = Button(frame, text=3, height=4, width=9, font=35, command= lambda: button_press(3))
button_3.grid(row=0, column=2)

button_4 = Button(frame, text=4, height=4, width=9, font=35, command= lambda: button_press(4))
button_4.grid(row=1, column=0)

button_5 = Button(frame, text=5, height=4, width=9, font=35, command= lambda: button_press(5))
button_5.grid(row=1, column=1)

button_6 = Button(frame, text=6, height=4, width=9, font=35, command= lambda: button_press(6))
button_6.grid(row=1, column=2)

button_7 = Button(frame, text=7, height=4, width=9, font=35, command= lambda: button_press(7))
button_7.grid(row=2, column=0)

button_8 = Button(frame, text=8, height=4, width=9, font=35, command= lambda: button_press(8))
button_8.grid(row=2, column=1)

button_9 = Button(frame, text=9, height=4, width=9, font=35, command= lambda: button_press(9))
button_9.grid(row=2, column=2)

button_0 = Button(frame, text=0, height=4, width=9, font=35, command= lambda: button_press(0))
button_0.grid(row=3, column=1)

minus = Button(frame, text="-", height=4, width=9, font=35, command= lambda: button_press("-"))
minus.grid(row=3, column=0)

plus = Button(frame, text="+", height=4, width=9, font=35, command= lambda: button_press("+"))
plus.grid(row=3, column=2)

multiply = Button(frame, text="*", height=4, width=9, font=35, command= lambda: button_press("*"))
multiply.grid(row=0, column=3)

divide = Button(frame, text="/", height=4, width=9, font=35, command= lambda: button_press("/"))
divide.grid(row=1, column=3)

equal = Button(frame, text="=", height=4, width=9, font=35, command= equals)
equal.grid(row=2, column=3)

decimal = Button(frame, text=".", height=4, width=9, font=35, command= lambda: button_press("."))
decimal.grid(row=3, column=3)

clear = Button(window, text="clear", height=4, width=15, font=35, command= clear)
clear.pack()
window.mainloop()