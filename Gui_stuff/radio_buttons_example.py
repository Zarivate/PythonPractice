# Radio buttons are similar to checkboxes but you can only select 1 from a group instead now

from tkinter import *

food = ['mole', 'torta', 'uranium']

def order():
    if (x.get() == 0):
        print("You have selected Mole, good man!")
    elif (x.get() == 1):
        print("You've chosen torta, simple but alright")
    elif (x.get() == 2):
        print("You've chosen uranium because you wanna die")
    else:
        print("What happened?")

window = Tk()

moleImage = PhotoImage(file='mole.png')
tortaImage = PhotoImage(file='torta.png')
uraniumImage = PhotoImage(file='uranium.png')
food_Images = [moleImage, tortaImage, uraniumImage]

x = IntVar()

for index in range(len(food)):
    # Each item gets its  own value because if not, then anytime one is clicked then they're all clicked
    radiobutton = Radiobutton(window,
                              text=food[index], # adds text to radio buttons
                              variable=x, # Groups radio buttons together if they share the same value
                              value=index,# assigns each radio button a different value
                              padx=25,
                              font=('Arial', 30),
                              image=food_Images[index],
                              compound='left',
                              indicatoron=False,
                              width= 400,
                              command=order
                              )

    radiobutton.pack(anchor=W)

window.mainloop()