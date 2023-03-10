import random
from tkinter import *

# Constants
WIDTH = 700
HEIGHT = 700
SNAKE_SPEED = 50
# How large game items are
ITEM_SIZE = 25
# How many parts does the snake have
SNAKE_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = 'yellow'
BG_COLOR = "black"

class Snake:

    def __init__(self):
        self.body_size = SNAKE_PARTS
        self.coordinates = []
        # Squares for that will make up the snake itself
        self.squares = []

        # Makes it so snake starts off in top left of screen every game
        for i in range(0, SNAKE_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            # Create list of squares to append to another list
            square = canvas.create_rectangle(x, y, x + ITEM_SIZE, y + ITEM_SIZE, fill=SNAKE_COLOR, tag='snake')
            self.squares.append(square)

class Food:

    def __init__(self):

        # Place food pellet on random place on board
        x = random.randint(0, (WIDTH/ITEM_SIZE)-1) * ITEM_SIZE
        y = random.randint(0, (HEIGHT/ITEM_SIZE) - 1) * ITEM_SIZE

        self.coordinates = [x,y]

        # Create food object on board
        canvas.create_oval(x, y, x + ITEM_SIZE, y + ITEM_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    # Unpack head of snake
    x, y = snake.coordinates[0]

    if direction == "up":
        # Move one space up
        y -= ITEM_SIZE

    elif direction == "down":
        y += ITEM_SIZE

    elif direction == "left":
        x -= ITEM_SIZE

    elif direction == "right":
        x += ITEM_SIZE

    # Update coordinates of head of snake before updating window. New coordinates are inserted at the start/head of
    # the list.
    snake.coordinates.insert(0, (x,y))

    # Create new graphic for head of snake
    square = canvas.create_rectangle(x, y, x + ITEM_SIZE, y + ITEM_SIZE, fill=SNAKE_COLOR)

    # Update snake list of squares
    snake.squares.insert(0, square)

    # Checks to see if coordinates overlap with food coordinates so food pellet can be removed and score can be updated
    if x == food.coordinates[0] and y == food.coordinates[1]:

        # Update score, delete food object, and create new food object
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()


    else:
        # Delete last body part of snake, update canvas, and remove last square from list of squares before updating
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SNAKE_SPEED, next_turn, snake, food)

def change_direction(new_direction):

    # Old direction that will be changed
    global direction

    if new_direction == 'left':
        # This is to make sure that a 180-degree turn isn't done
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    # Unpack head of snake again
    x, y = snake.coordinates[0]

    # Check if crossed left or right border of game
    if x < 0 or x >= WIDTH:
        return True
    elif y < 0 or y >= HEIGHT:
        return True

    # Check to see if snake ever touches its own body parts, check for everything besides the head of the snake
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True

    return False


def game_over():

    # Erase the canvas and print some game over text
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=("Chiller", 50), text="GAME OVER!",
                       fill='red', tag="gameover")

window = Tk()

window.title("Snek game")
# So game window can't be resized
window.resizable(False, False)

score = 0
direction = "down"

# Score label
label = Label(window, text="Score:{}".format(score), font=("Consolas", 35))
label.pack()

# Game board emulated with a canvas
canvas = Canvas(window, bg=BG_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

# Center game window once it pops up
window.update()
window_height = window.winfo_height()
window_width = window.winfo_width()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Get the middle positions of the user's screen so can place game window in middle
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

# Creation of class objects
snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
