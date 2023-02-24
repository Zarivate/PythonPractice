from tkinter import *
from tkinter import filedialog

def open_a_file():
    # Returns a string corresponding to where chosen file/filepath is located
    file_path = filedialog.askopenfilename(initialdir='C:\\Users\\yourUsernameHere\\Desktop\\Projects\\PythonShennanigans\\file_dialogue_ex'
                                           , title='Gonna open a file?',
                                           filetypes=(("Text files","*.txt"),
                                           ('All files', "*.*")))
    print(file_path)
    file = open(file_path, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(text="Open a file", command=open_a_file)
button.pack()
window.mainloop()