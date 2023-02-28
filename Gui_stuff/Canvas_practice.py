# Canvas in Python is another widget although one that's used to draw graphs, plots, images in a window, etc
from tkinter import *

window = Tk()

# Like in other GUI widgets, there are coordinates you can specify items to be bound to. They change
# depending on how large you make the canvas' width and height
canvas = Canvas(window, height=500, width=500)
# Need coordinates of starting and ending position to make a line.
canvas.create_line(0,0, 500, 500, fill='red', width=3)
# When making ones that overlap, the most recently created one will be on top/take priority. So the blue line here
# Will be the color shown over the red one under it
canvas.create_line(0,500, 500, 0, fill='blue', width=3)
canvas.create_rectangle(50,50,250,250, fill='green', outline='blue')

# Can also pass in a list of points instead of direct coordinates too
polygon_points = [250,0,500,500,0,500]
canvas.create_polygon(polygon_points, fill='yellow', outline='black', width=3)

# What is being set with the coordinates is actually how much space the arc should take up
canvas.create_arc(0, 0, 500, 500)
canvas.pack()

window.mainloop()