from tkinter import *

def actionEvent(event):
    # .keysym
    print("You pressed: " + event.keysym)
    # Edit the label on the window screen to display whatever the user typed in
    label.config(text=event.keysym)

window = Tk()

# The <Key> is what makes the window watch out for any keyboard taps
window.bind("<Key>", actionEvent)

label = Label(window, font=("Chiller", 75))
label.pack()

window.mainloop()