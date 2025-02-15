print("""                                         
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l',\
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',\
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',\
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']        

def cipher(text, shift, direction):
    encrypted_text = []
    if direction == "decode":
                shift *= -1
    for letter in text:
        if letter in alphabet:
            index_of_letter = alphabet.index(letter)
            new_position = index_of_letter + shift
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += letter
    encrypted_text = ''.join(encrypted_text)
    print(f"The {direction}ed text is {encrypted_text}")

want_to_continue = True
while want_to_continue == True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    cipher(text, shift, direction)
    answer = input("Want to continue? 'Yes' or 'No'? ").lower()
    if answer == "yes":
        want_to_continue = True
    else:
        print("Finished.")
        break
