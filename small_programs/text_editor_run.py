from tkinter import *
import os
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    pass

# Because a lot more things are needed to change the font a variety of arguments is what's taken
def change_font(*args):
    pass

def new_file():
    pass

def open_file():
    pass

def save_file():
    pass

def cut():
    pass

def copy():
    pass

def paste():
    pass

def about():
    pass

def quit():
    pass


window = Tk()
window.title("Text Editor exercise")

# This is to figure out how much the window will be moved on the x and y-axis
window_height = 500
window_width = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# Variable to hold the current font
font_name = StringVar(window)
font_name.set("Chiller")

# Same idea but for size of font now
font_size = StringVar(window)
font_size.set("30")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)

# So text area can expand, grid_rowconfigure is used, weight is 1 so doesn't back expand
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
# This is so text area takes up most of the window, should also automatically go to next line once reaches end of
# width of box unless window is resized
text_area.grid(sticky=N + E + S + W)

window.mainloop()