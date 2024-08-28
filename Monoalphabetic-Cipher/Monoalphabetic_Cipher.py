import string
import random

def monoalphabetic_cipher(text, key, encrypt=True):
    if encrypt:
        key_map = {original: substitute for original, substitute in zip(string.ascii_uppercase + string.ascii_lowercase, key)}
    else:
        key_map = {substitute: original for original, substitute in zip(string.ascii_uppercase + string.ascii_lowercase, key)}

    result = ""
    for char in text:
        result += key_map.get(char, char)
    
    return result
        


def generate_monoalphabetic_key():
    characters = list(string.ascii_uppercase)
    random.shuffle(characters)
    return ''.join(characters)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


print("Welcome to the Cipher Program")
while True:
    print("\nMenu:")
    print("1. Encrypt using Monoalphabetic Cipher")
    print("2. Decrypt using Monoalphabetic Cipher")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '3':
        break
    
    filename = input("Enter the filename: ")
    content = read_file(filename)
    
    if choice == '1':
        key = generate_monoalphabetic_key()
        print("Generated key:", key)
        encrypted_content = monoalphabetic_cipher(content, key, encrypt=True)
        output_filename = input("Enter the output filename: ")
        write_file(output_filename, encrypted_content)
        print("Encryption complete. Check the file:", output_filename)
        
    elif choice == '2':
        key = input("Enter the key: ")
        decrypted_content = monoalphabetic_cipher(content, key, encrypt=False)
        output_filename = input("Enter the output filename: ")
        write_file(output_filename, decrypted_content)
        print("Decryption complete. Check the file:", output_filename)
        
    else:
        print("Invalid choice. Please try again.")