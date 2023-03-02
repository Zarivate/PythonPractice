from tkinter import *

window = Tk()

# Starting off by moving a simple widget first before moving onto image
window.geometry("500x500")

my_Image = PhotoImage(file='food.png')
label = Label(window, image=my_Image, bg='blue')


window.mainloop()