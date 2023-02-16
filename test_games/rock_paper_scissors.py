# Simple rock paper scissors game using what has been learned up too now

import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = ""

    # The .lower() is just a workaround too if a user types in all caps since the choices are case-sensitive
    while player not in choices:
        player = input("Please choose either rock, paper, or scissors: ").lower()

    if player == computer:
        print("Computer has: ", computer)
        print("Player has: ", player)
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer has: ", computer)
            print("Player has: ", player)
            print("You lose!")
        if computer == "scissors":
            print("Computer has: ", computer)
            print("Player has: ", player)
            print("Victory!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer has: ", computer)
            print("Player has: ", player)
            print("You lose!")
        if computer == "rock":
            print("Computer has: ", computer)
            print("Player has: ", player)
            print("Victory!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer has: ", computer)
            print("Player has: ", player)
            print("You lose!")
        if computer == "paper":
            print("Computer has: ", computer)
            print("Player has: ", player)
            print("Victory!")

    play_again = input("Would you like to play again? Please enter either yes or no: ").lower()

    if play_again != "yes":
        break
print("Thank you for playing!")
