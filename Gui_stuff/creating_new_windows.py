# Multiple ways of doing so, these are just two common ones
from tkinter import *

def create_a_window():
    # Can either use Tk or Toplevel()
    # What this one does is that it creates a new window, "on top" of other windows, has the effect of being
    # linked to a 'bottom' window. The top one being the newly create one while the bottom is the previous one
    # If you close the bottom window, you also close the one on top of it but not vice versa
    # new_window = Toplevel()

    # Can also just use Tk() again, this makes it so the windows are not connected to each other, meaning the
    # original window can be closed without closing the other
    new_window2 = Tk()

    # Close out old window after creating new one
    window.destroy()
window = Tk()

Button(window, text="Create a new window", command=create_a_window).pack()

window.mainloop()