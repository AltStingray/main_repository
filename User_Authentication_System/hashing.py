import hashlib

def encryption(data):
    data = bytes(data, "utf-8")
    encrypted_data = hashlib.sha3_256(data) 
    hex_representation = encrypted_data.hexdigest()
    return hex_representation
