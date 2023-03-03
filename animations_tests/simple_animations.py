# This focuses on simple image animation on a canvas, only moves main 4 directions. Up, left, down, and right.
from tkinter import *
import time

# Constant variable
WIDTH = 500
HEIGHT = 500
x_Velocity = 5
y_Velocity = 3

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background_photo = PhotoImage(file='meirl2.png')
background = canvas.create_image(0,0, image=background_photo, anchor=NW)

test_image = PhotoImage(file='meirl.png')
my_image = canvas.create_image(0,0, image=test_image, anchor=NW)

image_width = test_image.width()
image_height = test_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    # Condition to make it so image bounces off any walls it hits. The first and second values in coordinates[]
    # are x and y respectively. Have to factor in width of image when trying to get image to bounce back
    # correctly as well.
    if(coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0):
        # Makes x velocity negative/-1 in order to reverse its movement
        x_Velocity = -x_Velocity
    if (coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0):
        y_Velocity = -y_Velocity
    canvas.move(my_image, x_Velocity, y_Velocity)
    window.update()
    time.sleep(0.01)

window.mainloop()