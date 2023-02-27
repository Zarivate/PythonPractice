# Canvas in Python is another widget although one that's used to draw graphs, plots, images in a window, etc
from tkinter import *

window = Tk()

# Like in other GUI widgets, there are coordinates you can specify items to be bound to. They change
# depending on how large you make the canvas' width and height
canvas = Canvas(window, height=500, width=500)
# Need coordinates of starting and ending position to make a line.
canvas.create_line(0,0, 500, 500, fill='red', width=3)
# When making ones that overlap, the most recently created one will be on top/take priority
canvas.create_line(0,500, 500, 0, fill='blue', width=3)
canvas.pack()

window.mainloop()