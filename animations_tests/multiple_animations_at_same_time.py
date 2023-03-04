from tkinter import *
from Ball import *
import time

WIDTH= 500
HEIGHT = 500

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 1, 1, "blue")
green_ball = Ball(canvas, 0, 0, 50, 4, 3, "green")
small_ball = Ball(canvas, 0, 0, 10, 9, 8, "black")

while True:
    volley_ball.move()
    green_ball.move()
    small_ball.move()
    # So window refreshes and any changes are reflected
    window.update()
    time.sleep(0.01)

window.mainloop()