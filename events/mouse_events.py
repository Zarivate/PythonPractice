from tkinter import *

def doSomething(event):
    # The x and y here are the x and y coordinates of the button press
    print("You pressed something on the mouse at !" + str(event.x) + " " + str(event.y))

window = Tk()

# Is for left side button of mouse
window.bind("<Button-1>", doSomething)
# Scroll wheel press
window.bind("<Button-2>", doSomething)
# Right side mouse click
window.bind("<Button-3>", doSomething)
# Tracks when a button press is released
window.bind("<ButtonRelease>", doSomething)
# Keeps track of when a mouse enters the screen
window.bind("<Enter>", doSomething)
# Keeps track of when a cursor/mouse leaves the window
window.bind("<Leave>", doSomething)
# Useful for games, keeps constant track of mouse movement on window
window.bind("<Motion>", doSomething)

window.mainloop()