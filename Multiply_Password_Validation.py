import os
digit = ["0","1","2","3","4","5","6","7","8","9"]
symbol = ["#","!","@","$","%","&"]

def lower():
    for letter in password:
        if letter.islower():
            return True
def upper():
    for letter in password:
        if letter.isupper():
            return True
        
def digits_symbols(value):
    for one in password:
        if one in value:
            return True

def check(password):
    if len(password) >= 8:
        if lower():
            if upper():
                if digits_symbols(digit):
                    if digits_symbols(symbol):
                        return password
def validation():
    result = check(password)
    with open ("password_database.txt", "a") as database:
        if result == password:
            database.write(f"{password}\n")
            valid_pass.append(password)
        else:
            invalid_pass.append(password)
                
count = int(input("How many passwords do you want to validate? Number: "))

if os.path.exists("password_database.txt"):
    pass
else:
    database = open("password_database.txt", "x")
    
valid_pass = []
invalid_pass = []
for num in range(1, count + 1):
    password = input("Input password: ")
    validation()
    
os.system('cls')  

print("Valid passwords: ")
for one in range(0, len(valid_pass)):
    print(valid_pass[one])
    
print("\nInvalid passwords: ")
for one in range(0, len(invalid_pass)):
    print(invalid_pass[one])