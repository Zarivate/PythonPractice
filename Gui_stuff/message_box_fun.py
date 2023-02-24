# Message boxes are what they sound like, boxes that appear on your screen with a message. Usually an alert of sorts

from tkinter import *
from tkinter import messagebox

def click():
    # Message box creation, multiple possible types
    #m essagebox.showinfo(title="This is an info message box",
                        # message="You exist!")
    # Setting this one equal to True in a while loop is common scammer practice
    # messagebox.showwarning(title="This is an info message box",
                        # message="You exist!")
    # messagebox.showerror(title="This is an info message box",message="You exist!")

    # This one returns true or false
    # if messagebox.askokcancel(title='Ask ok cancel?', message="Do you agree?"):
    #     print("You returned true, you fool")
    # else:
    #     print("You returned false, you fool")

    # This one does as well, just with different text options now
    # if messagebox.askretrycancel(title='Ask ok cancel?', message="Do you agree?"):
    #     print("You retried, you fool")
    # else:
    #     print("You cancelled, you fool")

    # if messagebox.askyesno(title='Ask yes no?', message="Do you like turtles?"):
    #     print("Good man")
    # else:
    #     print("Poor taste")

    # This one is a bit different in that it returns a string of "yes" or "no"
    # answer = messagebox.askquestion(title="Ask question box", message="Do you exist?")
    # if answer == 'yes':
    #     print("I knew you were alive")
    # else:
    #     print("How did you do this?")

    # This one returns 3 possible strings, "True", "False", or "None". Also you could change the icon around to
    # whichever one you feel is most appropriate
    answer = messagebox.askyesnocancel(title='Yes no cancel?', message='Are you happy?', icon='error')
    print(answer)

window = Tk()

button = Button(window, command=click, text='Click me if you dare')
button.pack()

window.mainloop()