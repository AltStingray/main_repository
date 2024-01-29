import hashlib

data_bytes = bytes(input("Input your data you want to hash: "), "utf-8")
#utf-8 is a standard character encoding format, it translate all the text into bytes
# you can also represent it as data_bytes = data.encode('utf-8') 

def encryption(data):
    encrypted_data = hashlib.sha3_256(data) #sha3_256 is even more secure
    hex_representation = encrypted_data.hexdigest()
    return hex_representation
    
print(f"Your hashed data in hex representation is: \n{encryption(data_bytes)}")
