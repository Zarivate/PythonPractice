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


# Mimics creation of a new window by resetting the title of the window alongside any written text
def new_file():
    window.title("Undefined")
    # Delete all the text within the file from the start to the very end
    text_area.delete(1.0, END)

def open_file():
    file = askopenfilename(defaultextension=".txt", file=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, 'r')
        text_area.insert(1.0, file.read())
    except Exception:
        print("Couldn't read file, sorry.")

    finally:
        file.close()

def save_file():
    file = filedialog.asksaveasfilename(initialfile="bingus.txt",
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    # If user closes out of filedialog, just return
    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        # Better to specify exceptions instead of using a general one but for now this is fine
        except Exception:
            print("Something went wrong and file couldn't be saved.")

        finally:
            file.close()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

# Mimics paste command
def paste():
    text_area.event_generate("<<Paste>>")

# A simple pop up given information about the program itself
def about():
    # Title of pop-up window followed by text within the window itself
    showinfo("Info about this program", "A simple program meant to help put multiple concepts together for learning.")

# Closes out window
def quit():
    window.destroy()


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
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=quit)

# Second dropdown menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label='Cut', command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

# Third dropdown menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()