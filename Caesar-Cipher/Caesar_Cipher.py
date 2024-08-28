import string
import random

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    if not encrypt:
        shift = -shift
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

print("Welcome to the Cipher Program")
while True:
    print("\nMenu:")
    print("1. Encrypt using Caesar Cipher")
    print("2. Decrypt using Caesar Cipher")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '3':
        break 
    
    if choice == '1':
        shift = int(input("Enter the shift value: "))
        content = read_file("sender.txt")
        encrypted_content = caesar_cipher(content, shift, encrypt=True)
        write_file("encripted.txt", encrypted_content)
        print("Encryption complete. Check the file: encripted.txt")
        
    elif choice == '2':
        shift = int(input("Enter the shift value: "))
        content = read_file("encripted.txt")
        decrypted_content = caesar_cipher(content, shift, encrypt=False)
        write_file("decripted.txt", decrypted_content)
        print("Decryption complete. Check the file: decripted.txt")

    else:
        print("Invalid choice. Please try again.")
