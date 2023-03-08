from tkinter import *
import os
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    # Color variable holds a tuple, only one of the variables is needed however so how to get correct index
    color = colorchooser.askcolor(title='Pick a color or die')
    text_area.config(fg=color[1])


# Because a lot more things are needed to change the font a variety of arguments is what's taken
def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

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
# Makes it so window automatically scrolls down when user hits bottom of window
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

# Frame to hold extra widgets
frame = Frame(window)
frame.grid()

color_button = Button(frame, text='color', command=change_color)
color_button.grid(row=0, column=0)

# In order to get all possible fonts, can use families() function on *font/all the fonts. Will return all the
# different fonts available
font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

# When the spinbox is used and the change_font() command is called, the font_size is what will be passed in.
# It is why the change_font() function takes a varied amount of arguments
size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

# Menubar section that holds a cascading option list for the user
menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade()

window.mainloop()