# A label is an area widget that holds text and/or an image within a window
from tkinter import *

window = Tk()

image_to_be_used = PhotoImage(file='logo.png')

# Many parameters exist to customize a label, relief being to customize the border style, border width=bd
# compound is so both the image and text appear
label = Label(window,
              text="Howdy there",
              font=('Arial', 45, 'italic'),
              fg="#5cfcff",
              bg='black',
              relief=RAISED,
              bd=20,
              padx=20,
              pady=20,
              image=image_to_be_used,
              compound='bottom')
# Sets label right in middle of window
label.pack()
# Set label to a custom location in window
# label.place(x=0, y=0)

window.mainloop()