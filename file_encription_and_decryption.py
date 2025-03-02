from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(filename + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File '{filename}' encrypted successfully!")

def decrypt_file(encrypted_filename, key):
    fernet = Fernet(key)
    with open(encrypted_filename, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(encrypted_filename.replace(".enc", ""), "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    print(f"File '{encrypted_filename}' decrypted successfully!")

if __name__ == "__main__":
    generate_key() 
    key = load_key()
    
    file_to_encrypt = "example.txt"  
    encrypt_file(file_to_encrypt, key)
    
    file_to_decrypt = file_to_encrypt + ".enc"
    decrypt_file(file_to_decrypt, key)

