from tkinter import *

window = Tk()

menuBar = Menu(window)

window.config(menu=menuBar)

# Gets added to previous menubar instead of to the window itself
fileMenu = Menu(menuBar)

# Makes it so it drops down
menuBar.add_cascade()

window.mainloop()