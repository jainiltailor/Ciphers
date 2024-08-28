import math

def encrypt_transposition_cipher(plaintext, key):
    # Calculate the number of columns and rows needed
    num_columns = len(key)
    num_rows = math.ceil(len(plaintext) / num_columns)
    grid = [''] * num_columns
    
    # Fill the grid column by column according to the key order
    for index, char in enumerate(plaintext):
        column = index % num_columns
        grid[column] += char

    # Read columns in the order of the key to generate ciphertext
    sorted_key = sorted(list(key))
    ciphertext = ''
    for char in sorted_key:
        column_index = key.index(char)
        ciphertext += grid[column_index]
    
    return ciphertext


def decrypt_transposition_cipher(ciphertext, key):
    # Calculate the number of columns and rows needed
    num_columns = len(key)
    num_rows = math.ceil(len(ciphertext) / num_columns)
    num_empty_cells = num_columns * num_rows - len(ciphertext)
    
    # Prepare grid for decryption
    grid = [''] * num_columns
    sorted_key = sorted(list(key))
    index = 0
    
    for char in sorted_key:
        column_index = key.index(char)
        if column_index < num_columns - num_empty_cells:
            grid[column_index] = ciphertext[index:index + num_rows]
            index += num_rows
        else:
            grid[column_index] = ciphertext[index:index + num_rows - 1]
            index += num_rows - 1
    
    # Read the plaintext row by row
    plaintext = ''
    for i in range(num_rows):
        for column in grid:
            if i < len(column):
                plaintext += column[i]
    
    return plaintext

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

while True:
    print("\nMenu:")
    print("1. Encrypt using Transposition Cipher")
    print("2. Decrypt using Transposition Cipher")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 3:
        break
    
    filename = input("Enter the filename: ")
    key = input("Enter the key: ")
    content = read_file(filename)    
    if choice == 1:
        encrypted_content = encrypt_transposition_cipher(content, key)
        print("Encrypted content: " + encrypted_content)
        output_filename = input("Enter the output filename: ")
        write_file(output_filename, encrypted_content)
        print("Encryption complete. Check the file:", output_filename)
        
    elif choice == 2:
        decrypted_content = decrypt_transposition_cipher(content, key)
        print("Decrypted content: " + decrypted_content)
        output_filename = input("Enter the output filename: ")
        write_file(output_filename, decrypted_content)
        print("Decryption complete. Check the file:", output_filename)
        
    else:
        print("Invalid choice. Please try again.")
