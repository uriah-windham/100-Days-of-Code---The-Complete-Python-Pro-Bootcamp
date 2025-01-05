import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
generated_password_list = []
generated_password = ""
password_character_count = 0

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your character?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for letter in range(0, nr_letters):
    generated_password_list.append(random.choice(letters))
    password_character_count += 1

for symbol in range(0, nr_symbols):
    generated_password_list.append(random.choice(symbols))
    password_character_count += 1

for number in range(0, nr_numbers):
    generated_password_list.append(random.choice(numbers))
    password_character_count += 1

random.shuffle(generated_password_list)

for character in generated_password_list:
    generated_password += character

print(f"You character is: {generated_password}")