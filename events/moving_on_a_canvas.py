# Pseudo sequel to moving images with keys
from tkinter import *

# Functions to handle movement of photo image, slightly different from before
def move_up(event):
    # Takes 3 arguments, image that is being moved, how many pixels on x-axis want to move, and same for y-axis
    canvas.move(my_Image, 0, -10)
def move_down(event):
    canvas.move(my_Image, 0, 10)
def move_left(event):
    canvas.move(my_Image, -10, 0)
def move_right(event):
    canvas.move(my_Image, +10, 0)

window = Tk()

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

test_Image = PhotoImage(file='food.png')
# The anchor here is just so the image isn't cut off near the top left corner
my_Image = canvas.create_image(0,0, image=test_Image, anchor=NW)

window.mainloop()