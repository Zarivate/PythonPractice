from tkinter import *
from tkinter import filedialog

def openFile():
    file_path = filedialog.askopenfilename(
        title='Gonna open a file?',
        filetypes=(("Text files", "*.txt"),
                   ('All files', "*.*")))
    print(file_path)
    file = open(file_path, 'r')
    print(file.read())
    file.close()

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("All files", ".*")
                                    ])
    # Prevents an error from happening when user exits window without saving and or creating a file
    if file is None:
        return

    file_text = str(text.get('1.0', END))
    file.write(file_text)
    file.close()

def bingusGo():
    print("Bingus confirmed")

def cut():
    print("Cut confirmed")

def copy():
    print("Copy has happened")

def paste():
    print("Paste has happened")

window = Tk()

openImage = PhotoImage(file='torta.png')
saveImage = PhotoImage(file='mole.png')
exitImage = PhotoImage(file='uranium.png')

menuBar = Menu(window)

window.config(menu=menuBar)
text = Text(window, font=("Chiller", 25), width=20, height=10, bg='light yellow', pady=10, padx=10)
text.pack()

# Gets added to previous menubar instead of to the window itself. The tear-off option is to remove the annoying
# dash of lines set by default in a drop-down menu
fileMenu = Menu(menuBar, tearoff=0, font=('Chiller', 25))

# Makes it so it drops down
menuBar.add_cascade(label="File", menu=fileMenu)
# Clickable option for the drop-down menu
fileMenu.add_command(label="Open", command=openFile, image=openImage, compound='left')
fileMenu.add_command(label="Save", command=saveFile, image=saveImage, compound='left')
fileMenu.add_command(label="Bingus", command=bingusGo, image=exitImage, compound='left')
# Adds separator line between the drop-down options. This one adds a line between Bingus and Exit
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menuBar, tearoff=0,font=('Chiller', 25))
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()