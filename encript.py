from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    
    with open(input_file, 'rb') as file:
        original = file.read()
    
    encrypted = fernet.encrypt(original)
    
    with open(output_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Generar una nueva clave (esto se hace una sola vez)
generate_key()

# Cargar la clave
key = load_key()

# Encriptar el archivo
encrypt_file('variables.py', 'variables.enc', key)
