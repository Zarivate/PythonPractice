from tkinter import *
# Need this module so can have access to notebook widget
from tkinter import ttk

window = Tk()

# Widget that manages a collection of windows and displays
notebook = ttk.Notebook(window)

# Adding frame to notebook for first tab
tab_1 = Frame(notebook)
tab_2 = Frame(notebook)
tab_3 = Frame(notebook)

notebook.add(tab_1, text="Tab 1")
notebook.add(tab_2, text="Tab 2")
notebook.add(tab_3, text="Tab 3")
# What expand does here is that it expands to fill any space that would otherwise not be used, is so that
# What fill does is that it makes it so the content stays in the top left by filling up any empty space on both sides
notebook.pack(expand=True, fill="both")

# Labels for the notebook, tab_1 is the parent widget here
Label(tab_1, text="Hello this is tab 1!", width=50, height=25).pack()
Label(tab_2, text="Hello this is tab 2!", width=50, height=25).pack()
Label(tab_3, text="Hello this is tab 3!", width=50, height=25).pack()

window.mainloop()