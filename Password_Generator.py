"""
Password Generator

Generates a random and secure password based on user-defined
numbers of letters, symbols, and digits.
"""
import random

letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []

# Add letters
for _ in range(nr_letters):
    password.append(random.choice(letters))

# Add symbols
for _ in range(nr_symbols):
    password.append(random.choice(symbols))

# Add numbers
for _ in range(nr_numbers):
    password.append(random.choice(numbers))

# Shuffle password
random.shuffle(password)

# Convert list to string
final_password = "".join(password)
print(f"Your password is: {final_password}")
