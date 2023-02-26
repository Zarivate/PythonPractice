# Frames are a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

# The frame gets buttons added to it below while the frame itself is what gets set to the window
frame = Frame(window, bg='yellow', bd=5, relief=RAISED)
# Depending on which side it's set to, it'll stick to that side no matter how large the window becomes
# frame.pack(side=BOTTOM)

# Also have access to place() to set certain coordinate positions for a frame
frame.place(x=100, y=100)

# You don't have to set a variable equal to this if you don't plan n using it for much and or very long
# It's why we don't have button =, like we normally would
Button(frame, text="W", font=("Chiller", 25), width=3).pack(side=TOP)
Button(frame, text="A", font=("Chiller", 25), width=3).pack(side=LEFT)
Button(frame, text="S", font=("Chiller", 25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("Chiller", 25), width=3).pack(side=LEFT)

window.mainloop()