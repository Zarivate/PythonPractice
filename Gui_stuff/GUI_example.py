# There are two main things that go into a GUI
# 1. Widgets = GUI elements such as: buttons, text-boxes, labels, images, etc
# 2. Windows = containers meant to hold or contain the widgets

from tkinter import *

# Instantiate an instance of a window
window = Tk()
# Resize window
window.geometry("550x551")
# Change window title
window.title("If you're reading this that means it was done right")
# Change window icon to something imported, has to be converted into a usable PhotoImage format too
icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)

# Change aspects of the window,
window.config(background="#5cfcff")

# Place window on screen, listen for events as well
window.mainloop()