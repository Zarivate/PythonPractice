import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# This is a basic Python program that uses user input to keep track of any passwords and encrypt them.
# Any passwords are stored in a created text file.


# Function to create the encryption key file
def make_key(pwd):
    key = base64.urlsafe_b64encode(kdf.derive(pwd.encode()))
    # Create a file to store the key
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# Function to actually get the key
def load_key():
    # Read the file using read bytes mode
    file = open("key.key", "rb")
    # Store the key in a variable
    key = file.read()
    file.close()
    return key


salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=480000,
)

# Get user input to be used for master password. Will be used to encrypt and check if user has permission to view data.
master_pwd = input("What is the master password? ")
actual_key = load_key()
possible_key = base64.urlsafe_b64encode(kdf.derive(master_pwd.encode()))
if possible_key == actual_key:
    possible_key = actual_key
else:
    print("That is not the right password. Please try again.")
fer = Fernet(possible_key)


# Function to view the passwords
def view():
    # Read the contents of the file to the user
    with open("passwords_example.txt", "r") as file:
        # Read all the lines of the file
        for line in file.readlines():
            data = line.rstrip()
            username, password = data.split("|")
            # Decrypt password before printing out to user. In order to make sure they have the correct password.
            print("Username:", username, "| Password:", fer.decrypt(password.encode()).decode())


# Function to add a password
def add():
    name = input("Please enter a username: ")
    password = input("Please enter a password: ")

    # Append password to file if already exists, else create the file and append the data
    with open("passwords_example.txt", "a") as file:
        # Encode password using encryption function, is decoded so can be properly added to file without worrying about
        # syntax issues when writing. Will take the byte string and convert it to a regular string.
        file.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a password or view existing ones? (view, add) Type in q to quit. ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please type in either view or add")
        continue
