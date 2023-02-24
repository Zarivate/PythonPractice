# A text widget functions much the same as a text area, both can be used to enter multiple lines of text

from tkinter import *

def submit():
    # Gets text from text are/what user typed in. The 1.0 and END are saying that we want everything from the
    # first line (starting index) to the last line (Ending index)
    input = text.get('1.0', END)
    print(input)

window = Tk()

# Careful when changing the font size as it directly corresponds to how big the window will appear unless
# height and width are also changed
text = Text(window,
            bg='light yellow',
            font=('Ink Free', 15),
            height=8,
            width=20,
            padx=10,
            pady=10,
            fg='black')
text.pack()

button = Button(window, text='Submit', command=submit)
button.pack()

window.mainloop()