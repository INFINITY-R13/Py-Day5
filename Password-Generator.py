import random

# Lists of characters to choose from
letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('!#$%&*+')

print("Welcome to the PyPassword Generator!")

# Get user input for character counts
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level: Letters, symbols, and numbers in order
password_easy = ""

for _ in range(nr_letters):
    password_easy += random.choice(letters)
for _ in range(nr_symbols):
    password_easy += random.choice(symbols)
for _ in range(nr_numbers):
    password_easy += random.choice(numbers)

print(f"Easy Level Password: {password_easy}")

# Hard Level: Letters, symbols, numbers shuffled
password_chars = []

for _ in range(nr_letters):
    password_chars.append(random.choice(letters))
for _ in range(nr_symbols):
    password_chars.append(random.choice(symbols))
for _ in range(nr_numbers):
    password_chars.append(random.choice(numbers))

random.shuffle(password_chars)  # Shuffle list elements

password_hard = ''.join(password_chars)  # Join list into string

print(f"Hard Level Password: {password_hard}")
