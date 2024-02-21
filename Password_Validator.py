# you could also use 'import re' to simplify the process
print("Welcome to password validator!\n")

digit = ["0","1","2","3","4","5","6","7","8","9"]
symbol = ["#","!","@","$","%","&"]

def digits():
    for num in password:
        if num in digit:
            return True
        
def symbols():
    for sym in password:
        if sym in symbol:
            return True       

def validation():
    lower = 0
    upper = 0
    for char in password:
        if char.islower():
            lower += 1
        if char.isupper():
            upper += 1
                              
    if len(password) < 8:
        return False
    if lower == 0:
        return "lower letter"
    if upper == 0:
        return "upper letter"   
    if digits() != True:
        return "digit"
    if symbols() != True:
        return "symbol"
        
password = input("Input password you want to check: ")

valid = validation()

if valid == False:
    print("Password does not meet requiremetns. \nMinimal length of digits have to be 8.")
elif valid == "lower letter" or valid == "upper letter" or valid == "digit" or valid == "symbol":
    print(f"Password does not meet requirements. At least one {valid} have to be specified.")
else:
    print("Valid password.")