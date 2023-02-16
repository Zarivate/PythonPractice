# A quiz game, skeleton functions for now
def new_game():
    guesses = []
    correct_guesses = 0
    question_position = 0

    for key in questions:
        print("----------------------------")
        print(key)
        for i in options[question_position]:
            print(i)
        guess = input("Please enter your choice (A, B, C, or D): ").upper()
        guesses.append(guess)
        # Call the function to check whether the guess is correct or not by
        # passing in the answer alongside the user's guess. Return a 1 if correct
        # or 0 if wrong so increment the correct guesses value from it
        correct_guesses += check_answer(questions.get(key), guess)
        question_position += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong, moron, go to jail!")
        return 0


def display_score(correct_ones, guesses):
    print("----------------------------")
    print("Results are in")
    print("----------------------------")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print("")

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print("")

    score = int((correct_ones/len(questions))*100)
    print("Your score is " + str(score) + "%")


def play_again():

    ask = input("Do you want to go another round? (yes/no): ").upper()

    if ask == "YES":
        return True
    else:
        return False


# Dictionary collection to hold key value pairs for questions to be asked. The questions will be
# asked in an A-D format, with the value being the correct choice
questions = {
    "What color is the SEGA logo?: ": "A",
    "What year did the original Sonic the Hedgehog release?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "What is the name of SEGA's flagship mascot?: ": "A",
}

# 2D list to hold the options for the  questions
options = [["A. Blue", "B. Red", "C. Orange", "D. Laser Lemon"],
           ["A. 1999", "B. 1991", "C. 2006", "D. 1995"],
           ["A. SNL", "B. Smosh", "C. Monty Python", "D. Bort Wilkins and the snow dogs"],
           ["A. Sonic", "B. Dankey Kang", "C. Quandale", "D. Mayro"]]

new_game()

while play_again():
    new_game()

print("Thank you so much for ta playing my game!")