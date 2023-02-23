#

from tkinter import *



def display():
    if (x.get() == 1):
        print("Agreement has been made, but why?")
    else:
        print("You have saved yourself.")

window = Tk()

x = IntVar()
image_to_be_used = PhotoImage(file='logo.png')
# The on and off values are the values that are held when the checkbox is checked and not checked, it's set to
# 1 and 0 by default
check_button = Checkbutton(window,
                           text="I agree to soul destruction",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial', 30),
                           fg='#5cfcff',
                           bg='black',
                           activeforeground='#5cfcff',
                           activebackground='black',
                           padx=25,
                           pady=15,
                           image=image_to_be_used,
                           compound=LEFT )

check_button.pack()
window.mainloop()