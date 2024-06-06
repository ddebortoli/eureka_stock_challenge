from cryptography.fernet import Fernet
from os import remove
# Note to eureka developer:
# In order to make this eassier to test I just dropped this way of decrypt, but my idea in production would be to obtain this key from environ variables.
def load_key():
    return open("secret.key", "rb").read()

def decrypt_file(input_file, key):
    fernet = Fernet(key)
    data = {}
    with open(input_file, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    
    decrypted = fernet.decrypt(encrypted)
    
    with open('temp_file.py', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    with open('temp_file.py', 'r') as file:
        data = file.read()

    remove('temp_file.py')
    return data
