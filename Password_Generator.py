import random

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', \
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', \
'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', \
'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


greetings = "Welcome to the password generator!"
print(greetings)
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like in your password?\n"))
numbers = int(input("How many numbers would you like in your password?\n"))

final_output = ""

for l in range(0, letters):
    random_letter = random.randint(0, len(letters_list) - 1)
    final_output += letters_list[random_letter]

for n in range(0, numbers):
    random_number = random.randint(0, len(numbers_list) - 1)
    final_output += numbers_list[random_number]

for s in range(0, symbols):
    random_symbol = random.randint(0, len(symbols_list) - 1)
    final_output += symbols_list[random_symbol]

random_final_output = random.sample(final_output, len(final_output)) 
final_output = ''.join(random_final_output)
print(final_output)