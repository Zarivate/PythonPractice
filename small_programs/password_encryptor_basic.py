# This is a basic Python program that uses user input to keep track of any passwords and encrypt them.
# Any passwords are stored in a created text file.

# Get user input to be used for master password. Will be used to encrypt and check if user has permission to view data.
master_pass = input("What is the master password? ")


# Function to view the passwords
def view():
    # Read the contents of the file to the user
    with open("password.txt", "r") as file:
        # Read all the lines of the file
        for line in file.readlines():
            data = line.rstrip()
            username, password = data.split("|")
            print("Username:", username, "Password:", password)


# Function to add a password
def add():
    name = input("Please enter a username: ")
    password = input("Please enter a password: ")

    # Append password to file if already exists, else create the file and append the data
    with open("password.txt", "a") as file:
        file.write(name + "|" + password + "\n")


while True:
    mode = input("Would you like to add another password or view existing ones? (view, add) Type in q to quit.").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please type in either view or add")
        continue

