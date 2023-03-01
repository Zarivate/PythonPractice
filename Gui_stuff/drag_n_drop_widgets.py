from tkinter import *

# Function to get the original position of where the user clicked on the label
def drag_start(event):
    # Made so is compatible with multiple widgets, not just one
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

# Function to get/create new x and y coordinates for the new position of the label
def drag_motion(event):
    widget = event.widget
    # Gets top left x coordinate of label relative to window
    x = widget.winfo_x() - widget.startX + event.x
    # The first variable is the bottom left of the label itself, relative to the window, the second variable is
    # the location of where the widget was clicked, and the last variable is where the widget is being dragged to
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

window = Tk()

label = Label(window, bg='blue', width=10, height=5)
# Set the coordinates of the label to a specific point
label.place(x=0, y=0)

label_2 = Label(window, bg='orange', width=10, height=5)
label_2.place(x=100, y =50)

# Keeps track of left button click
label.bind("<Button-1>", drag_start)
# Keeps track of left button click and any movement made while left click active
label.bind("<B1-Motion>", drag_motion)

label_2.bind("<Button-1>", drag_start)
label_2.bind("<B1-Motion>", drag_motion)

window.mainloop()