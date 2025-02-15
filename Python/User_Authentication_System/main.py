import requests
import time
import os
from email_check import EmailVer
from registration import RegistrationClass
from login import login_func
from login import take_username
from hashing import encryption
from add_to_database import add_to_database
#Create a database(textfile). If already created, use current one.
if os.path.exists("database.json"):
    database = open("database.json", "r")
else:
    database = open("database.json", "x")
    
#Log in or Register. Then ask for user inputs - email and password
to_continue = True
while to_continue:
    option = input("Choose an option: Log in / Register -> ").lower()
    os.system("cls")
    if option == "register":
        username = input("Enter your username: ")
        registration = RegistrationClass(username)
        email = input("Enter your email: ")
        #you can clear\tag this lines if you want to create multiple accounts with use of a single email, but that's not fair;)
        for line in database:
            while encryption(email) in line:
                os.system("cls")
                print("Given email already exists!")
                email = input("Re-enter email: ")
                #
        password = registration.password_acceptance()
        
        request = requests.get(f"https://api.hunter.io/v2/email-verifier?email={email}&api_key=7e1d63f8216ca7bfe85aad42e3649d23bd2ca724")
        while request.status_code != 200:
            print("Given email doesn't exist!")
            email = input("Re-enter your email: ")
            request = requests.get(f"https://api.hunter.io/v2/email-verifier?email={email}&api_key=7e1d63f8216ca7bfe85aad42e3649d23bd2ca724")
        
        #email verification process
        email_verification = EmailVer(email)
        email_verification.email_check(email)
        #adding data to database process
        add_to_database(email, password, username)
        
        time.sleep(4)
        os.system("cls")
    elif option == "log in":
        while login_func() != True:
            os.system("cls")
            print("Incorrect email or password!\n")
        break
    else:
        print("Wrong input, try again!")

print(f"Welcome to the system, {take_username()}.")
