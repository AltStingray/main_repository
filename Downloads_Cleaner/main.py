from extensions import extensions
import os
import shutil
from datetime import datetime

username = (os.environ.get("userprofile"))[9:] #the environmental variable value of "userprofile" is C:/users/username, so I cut off the beginning and took only username for the sake of simplicity

current_date = datetime.now().strftime("%Y-%m-%d")
    
def create_dir(path):
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
        
def send_file(file):
    for file_format in extensions:
        for ext in extensions[file_format]:
            if file.endswith(f".{ext}"):
                create_dir(f"C:/Users/{username}/Desktop/Sorted_files/{file_format}") # creating unique directory for multiple extensions of one category
                create_dir(f"C:/Users/{username}/Desktop/Sorted_files/{file_format}/{ext}_files") #creating direcrory for each extension
                try:
                    shutil.move(f"C:/Users/{username}/Downloads/{file}", f"C:/Users/{username}/Desktop/Sorted_files/{file_format}/{ext}_files") #moving files from Downloads to their destination
                except FileNotFoundError:
                    pass
                print(f"{file} successfully moved to the C:/Users/{username}/Desktop/Sorted_files/{file_format}/{ext}_files {current_date}\n") #report message
            else:
                pass
    
def main():
    entry_files = os.listdir(f"C:/Users/{username}/Downloads")
    for file in entry_files:
        send_file(file)
        
create_dir(f"C:/Users/{username}/Desktop/Sorted_files") #to create the Sorted_files folder

main()