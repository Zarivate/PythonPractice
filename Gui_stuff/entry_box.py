# Entry boxes/widgets are what they sound like, they're text-boxes that accept a single line of user input

from tkinter import *


def submit():
    user_input = entry.get()
    print(user_input)
    # Disable an entry box
    entry.config(state=DISABLED)

def delete():
    # Deletes all the characters of whatever the user typed in from the 0th position to the last position
    entry.delete(0, END)

def backspace():
    # Similar to delete button, except now it just deletes the last character
    entry.delete(len(entry.get())-1, END)


window = Tk()

# Instantiation of the entry box, the show parameter is useful so that only that character shows up on the screen
# when a user types something out
entry = Entry(window, font=('Arial', 45), fg="#5cfcff", bg='black', show='*')

# Set a default text value to appear in the entry box
entry.insert(0, 'Ooga Booga')

entry.pack(side=LEFT)

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()