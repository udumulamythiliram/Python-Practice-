#password generator

import random
import re


def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password 
    

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1 
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 1 
    

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"
    
print("1) Generate Password")
print("2) Check Password Strength")
while True:
    try:

        choice = input("Enter your choice:")

        if choice in ["1", "2"]:
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input type. Please enter a number.")





if choice == "1":
    while True:

        try:
            length = int(input("Enter the desired password length:"))
            if length < 0:
                print("Length cannot be negative. Please enter a positive integer.")
            elif length < 8:
                print("It's recommended to use a password of at least 8 characters for better security.")
            else:
                break
        except ValueError:
            print("Invalid input type. Please enter a number.")

    password = generate_password(length)
    print("Generated Password:", password)
elif choice == "2":
    password = input("Enter the password to check:")
    strength = check_password(password)
    print("Password Strength:", strength)
else:
    print("Invalid")