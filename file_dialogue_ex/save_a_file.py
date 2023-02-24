from tkinter import *
from tkinter import filedialog

# Need to list the types of file formats that the file can be saved as alongside having to actually write
# the text to the file, so it's saved with something actually inside it
def save_a_file():
    # Can alter the direct directory option as well here if you want a different directory to open when
    # you click on the button
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("All files", ".*")
                                    ])
    # Prevents an error from happening when user exits window without saving and or creating a file
    if file is None:
        return

    # Save user written text into a variable, but also convert it into a string
    file_text = str(text.get('1.0', END))
    # Can also use the console window to accept and save text into a file like so
    # file_text = input("Enter some text pls: ")
    file.write(file_text)
    file.close()

window = Tk()
button = Button(text='Save file', command=save_a_file)
button.pack()
text = Text(window)
text.pack()
window.mainloop()