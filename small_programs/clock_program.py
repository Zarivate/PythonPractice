from tkinter import *
from time import *

def update():
    # Use built-in time function to store the current time into a string variable to be used later
    current_time = strftime("%I:%M:%S %p")
    time_label.config(text=current_time)

    current_day = strftime("%A")
    day_label.config(text=current_day)

    current_date = strftime("%B %d, %Y")
    date_label.config(text=current_date)

    # Recursively call function again every 1000 milliseconds (1 second), so clock can be properly updated
    window.after(1000, update)

window = Tk()

time_label = Label(window, font=("Chiller", 60), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(window, font=("Arial", 30))
day_label.pack()

date_label = Label(window, font=("Arial", 35))
date_label.pack()

update()

window.mainloop()