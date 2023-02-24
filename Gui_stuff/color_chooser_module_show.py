from tkinter import *
from tkinter import colorchooser # submodule

def click():
    # Color is assigned to a variable, returns a tuple with the first value being 3 decimal values
    # representing the amount of RGB respectively of the chosen color and the second being the hex value
    color = colorchooser.askcolor()
    print(color)
    # Assigns the hexadecimal color value of the color variable above to a separate variable
    colorHex = color[1]
    # Change the background color
    window.config(bg=colorHex)
    # Could also transform all this into 1 line of code with this line
    # window.config(bg=colorchooser.askcolor()[1])

window = Tk()

window.geometry("550x550")
button = Button(text='Click me!',command=click)
button.pack()
window.mainloop()

