from hashing import encryption

class RegistrationClass():
    def __init__(self, username):
        self.username = username

    def password_acceptance(self):
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

        def check():
            if len(password) >= 8:
                if lower():
                    if upper():
                        if digits_symbols(digit):
                            if digits_symbols(symbol):
                                return True
                            else:
                                return("Password does not meet requirements. At least one symbol have to be specified.")
                        else:
                            return("Password does not meet requirements. At least one digit have to be specified.")
                    else:
                        return("Password does not meet requirements. At least one upper letter have to be specified.")
                else:
                    return("Password does not meet requirements. At least one lower letter have to be specified.")
            else:
                return("Password does not meet requirements. Minimal length have to be at least 8.")
         
        password = input("Enter your password: ")
        result = check()
        while result != True:
            password = input(f"\n{result}\nPlease re-enter: ")
            result = check()
            
        password_confirm = input("Confirm your password: ")
        while password != password_confirm:
            print("Password does not match. Please re-enter.")
            password_confirm = input("Enter your password: ")
        
        return password