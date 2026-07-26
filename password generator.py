import random
import string

print("      Random Password Generator      ")

#password length 
while True :
    try:
        length = int(input("Enter password length (minimum 4) : "))
        if length >= 4:
            break
        else:
            print("Password length should be minimum 4.")
    except ValueError:
        print("Please enter a valid number.")

#user choices
use_upper = input("Include uppercase letters ? (Y/N) :").lower()
use_lower = input("Include lowercase letters ? (Y/N) : ").lower()
use_digit = input("Include numbers ? (Y/N) : ").lower()
use_symbol = input("Include special characters ? (Y/N) : ").lower()

password = []
characters = ""

# Add chacters according to user
if use_upper == "y":
    characters += string.ascii_uppercase
password.append(random.choice(string.ascii_uppercase))

if use_lower == "y":
    characters += string.ascii_lowercase
    password.append(random.choice(string.ascii_lowercase))

if use_digit == "y":
    characters += string.digits
    password.append(random.choice(string.digits))

if use_symbol == "y":
    characters += string.punctuation
    password.append(random.choice(string.punctuation))

# check if user selected at least one option
if characters == "":
    print("\n ERROR : You must select at least one character type.")
    exit()

# Fill the remaining chacaters
while len(password) < length :
    password.append(random.choice(characters))

 #suffle the password 
random.shuffle(password)

#convert list to string
password = "".join(password) 

#final password
print("\n        Password Generated :       \n")
print(     password)

               
