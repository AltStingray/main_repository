from hashing import encryption
import json
import os
def add_to_database(email, password, username):
    password = encryption(password)
    email = encryption(email)
     
    file_size = os.path.getsize("database.json")
    if file_size == 0:
        with open("database.json", "w") as database:
            userdata = {"id 1":{"username": username, "email": email, "password": password}}
            json.dump(userdata, database, indent=1)
    else:
        json_list = []
        with open("database.json", "r") as database:
            json_list = json.load(database)
            id_num = 1
            for line in json_list:
                id_num += 1
        
        json_list.update({f"id {id_num}":{"username": username, "email": email, "password": password}})
    
        with open("database.json", "w") as database:
            json.dump(json_list, database, indent=1)
        

        
