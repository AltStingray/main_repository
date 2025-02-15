import smtplib
from email.message import EmailMessage
import random
import os
class EmailVer():
    
    def __init__(self, email):
        self.email = email
        self.code = ""
        
    def ver_code(self):
        for one in range(0, 4):
            random_digit = str(random.randint(0, 9))
            self.code += random_digit
        return self.code
    
    def email_check(self, email):
        #Creates SMTP session
        smtp = smtplib.SMTP("smtp.gmail.com", 587) #1 parameter - server location, 2-nd: 587 port number for Gmail
        #Start TLS for security
        smtp.starttls()
        #Authentication
        email_password = os.environ.get("EMAIL_PASSWORD") #for minor security purposes
        smtp.login("altstingray@gmail.com", email_password)
        #Message to sent
        msg = EmailMessage()
        msg["Subject"] = "Email Verification"
        msg["From"] = "altstingray@gmail.com"
        msg["To"] = email
        msg.set_content(f"Your verification code: {self.ver_code()}")
        #Sending the message
        print("Verification code has been sent to your email.")
        smtp.send_message(msg)
        #Verifying the email using 4 digit code
        while input("\nEnter the code: ") != self.code: print("\nInvalid code, please try again.")
        print("Email verification passed successfully. \nRegistration completed.")
        #Terminating the session
        smtp.quit()
