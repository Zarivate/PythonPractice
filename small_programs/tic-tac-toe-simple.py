import random
from tkinter import *


def next_turn(row, column):

    # Turn the current player into a global variable so can have access throughout the function
    global current_player

    # Check to see that the current position is empty and there is no winner
    if buttons[row][column]['text'] == "" and check_winner() is False:

        # Checks to see if the current player matches with the player variable held within the first position of the
        # players array, if so set that position to be equal to whatever symbol the current player is
        if current_player == players[0]:
            buttons[row][column]['text'] = current_player

            # If there is no winner, then swap the player for the following one and display that on the screen
            if check_winner() is False:
                current_player = players[1]
                label.config(text=(players[1] + "'s turn"))

            # If there is a winner, then display the winner on screen
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))

            elif check_winner() == "Tie":
                label.config(text="It's a tie")

        else:

            buttons[row][column]['text'] = current_player

            # If there is no winner, then swap the player for the following one and display that on the screen
            if check_winner() is False:
                current_player = players[0]
                label.config(text=(players[0] + "'s turn"))

            # If there is a winner, then display the winner on screen
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))

            elif check_winner() == "Tie":
                label.config(text="It's a tie")

def check_winner():
    # Checks for all possible horizontal win conditions
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            # Change color of winning combination for easier viewing
            buttons[row][0].config(bg='green')
            buttons[row][1].config(bg='green')
            buttons[row][2].config(bg='green')
            return True

    # Checks for all possible vertical win conditions
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg='green')
            buttons[1][column].config(bg='green')
            buttons[2][column].config(bg='green')
            return True

    # Checks for diagonal win conditions, from top left to bottom right and top right to bottom left
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True

    elif empty_spaces() is False:
        # Change color for all spaces
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

def empty_spaces():
    # Variable to account for all the available spaces on the board
    spaces = 9

    for row in range(3):
        for column in range(3):
            # If the space is already filled, then remove one from the space variable
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global current_player

    current_player = random.choice(players)

    label.config(text=current_player + "'s turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")


window = Tk()
window.title("Simple tic-tac-toe game")
players = ["x", "o"]
current_player = random.choice(players)
# 2D list of buttons to represent the spaces on the board
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

# Label to display whosoever turn it currently is
label = Label(text=current_player + "'s turn", font=("Consolas", 40))
label.pack(side="top")

restart_button = Button(text='restart', font=("Chiller", 25), command=new_game)
restart_button.pack(side="top")

# Holds all the buttons that are added to 2D buttons list above
frame = Frame(window)
frame.pack()

# Nested for loop to simplify adding a button to each spot on the board
for row in range(3):
    for column in range(3):
        # Adds a button to the frame, which is added to the window overall, in the exact position of each button
        buttons[row][column] = Button(frame, text="",
                                      font=("Consolas", 40),
                                      width=5,
                                      height=2,
                                      command= lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column )

window.mainloop()
