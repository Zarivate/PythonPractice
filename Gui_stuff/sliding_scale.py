
from tkinter import *

def submit():
    print("The temperature is left at " + str(scale.get()) + ' degrees C')

window = Tk()

best_image = PhotoImage(file='mole.png')
best_label = Label(image=best_image)
best_label.pack()

# Scale creation
scale = Scale(window,
              from_=100,
              to=0,
              length=500,
              font=('Arial', 25),
              tickinterval= 10, # Adds numeric indicators on scale
              resolution= 5 , # How much the slider increments by
              troughcolor='#5cfcff', # Color of slide bar
              fg='red',
              bg='black'
              )
# Set default value of slider/scale, formula is to set it in the middle in most cases
scale.set(((scale['from']-scale['to'])/2) + scale['to'])

scale.pack()

worst_image = PhotoImage(file='uranium.png')
worst_label = Label(image=worst_image)
worst_label.pack()

# Get current value of slider
button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()