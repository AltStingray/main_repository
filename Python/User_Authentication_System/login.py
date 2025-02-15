from hashing import encryption
import json
def login_func():
    global hashed_password
    global hashed_email
    #password hash function
    #if email hash in database, then check if the password hash matches the entered one, then print out username
    with open("database.json", "r") as database:
        database = json.loads(database.read())
        email = input("Enter your email address: ")
        password = input("Enter your password: ")
        hashed_email = encryption(email)
        hashed_password = encryption(password)
        check_email = False
        check_password = False
        for id_num in range(1, len(database) + 1):
            user_id = database[f"id {id_num}"]
            if hashed_email in user_id["email"]:
                check_email = True
            if hashed_password in user_id["password"]:
                check_password = True
        if check_email == True and check_password == True:
            return True

def take_username():
    with open("database.json", "r") as json_database:
        database = json.loads(json_database.read())
        for id_num in range(1, len(database) + 1): #we use items() on json dict to tap into these keys and extract value from them, but only if it is 1-st lvl dict
            user_id = database[f"id {id_num}"]
            if hashed_password in user_id["password"] and hashed_email in user_id["email"]:
                username = user_id["username"]
                break
        return username