# Buttons are exactly what they sound like, they're buttons. You click them and stuff happens.
# A common widget in GUIs

from tkinter import *

clicked = 0

def click():
    # So that clicked variable can be accessed anywhere
    global clicked
    clicked += 1
    print(clicked)

window = Tk()
image_to_be_used = PhotoImage(file='logo.png')
# The button is assigned to the window, no parentheses in the click because it's a callback function here
# The activeforeground is changed to the same as the fg alongside the activebackground so that
# it doesn't flash everytime it's clicked. State can be used to disable and or enable a button
button = Button(window,
                text="Click me if you dare",
                command=click,
                font=('Arial', 55),
                fg="#5cfcff",
                bg='black',
                activeforeground='#5cfcff',
                activebackground='black',
                state=ACTIVE,
                image=image_to_be_used,
                compound='bottom')
button.pack()

window.mainloop()