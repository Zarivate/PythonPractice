# A listbox is a listing of selectable text items within its own container

from tkinter import *

def submit():
    food = []
    for index in listbox.curselection():
        # Adds the selected items at the selected index range to the food array
        food.insert(index, listbox.get(index))
    print("You have selected ")
    for index in food:
        print(index)


def add():
    # Adds a new item into the list box
    listbox.insert(listbox.size(), entry_box.get())

    # Automatically update size of listbox
    listbox.config(height=listbox.size())


def delete():
    # Reversed is here so the index deletion work is done in reverse, because if it's done normally then
    # the index positions change once one is deleted, and it would leave the other undeleted
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Chiller', 45),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "borger")
listbox.insert(2, "mole")
listbox.insert(3, "c4")
listbox.insert(4, "radish")
listbox.insert(5, "soup")

# Config is usually used when you want an option to change, by doing it like this the size of the listbox adjusts
# dynamically
listbox.config(height=listbox.size())

# Custom entry box for if someone wants to type something in
entry_box = Entry(window)
entry_box.pack()

submit_button = Button(window, text='Submit', command=submit)
submit_button.pack()

add_button = Button(window, text='Add', command=add)
add_button.pack()

delete_button = Button(window, text='Delete', command=delete)
delete_button.pack()

window.mainloop()