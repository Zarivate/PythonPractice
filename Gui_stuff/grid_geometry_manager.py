# What grid() is/are is they're a useful way to organize widgets in a container. They're
# organized in a table-like structure. Akin to an Excel sheet with rows and columns that we can specify
# where we want things to appear in. By default, only have 1 row and column but can be changed by telling
# Python where to widgets should be place, if place doesn't exist it will be created for us.
from tkinter import *

window = Tk()

title_label = Label(window, text='Enter your private information', font=("Chiller", 25)).grid(row=0, column=0, columnspan=2)

# By default, grid items are placed on top of one another in one long column but their positions can be changed
# Because we adjusted the width, all of column 0 expands to accommodate the width
first_name_label = Label(window, text="First name: ", width=25, bg="blue").grid(row=1, column=0)
first_name_entrybox = Entry(window).grid(row=1, column=1)

last_name_label = Label(window, text="Last name: ", bg="yellow").grid(row=2, column=0)
last_name_entrybox = Entry(window).grid(row=2, column=1)

eemail_label = Label(window, text="Email: ", bg='green').grid(row=3, column=0)
email_entrybox = Entry(window).grid(row=3, column=1)

# The column span makes it so the widget is between the combined length of both of the columns. Will now
# take up the next 2 available columns, including its own. Makes it so its right in the middle.
submit_button = Button(window, text="Submit").grid(row=4, column=0, columnspan=2)

window.mainloop()
