import numpy as np

# Find the inverse of matrix under modulo 
def mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    matrix_modulus_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus) % modulus
    return matrix_modulus_inv

# Create matrix of given size from key string 
def create_matrix_from_key(key, size):
    key = [ord(char) - ord('A') for char in key]
    return np.array(key).reshape(size, size)

# Process text to fit the matrix size, padding with 'pad_char' if necessary 
def process_text(text, size, pad_char='X'):
    text = text.upper()
    text = text.replace(' ', '')
    while len(text) % size != 0:
        text += pad_char
    return text

# Convert text to numbers
def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]

# Convert numbers to text
def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

# Encryption function
def hill_encrypt(plaintext, key, size):
    original_spaces = [i for i, char in enumerate(plaintext) if char == ' ']
    plaintext = process_text(plaintext, size)
    key_matrix = create_matrix_from_key(key, size)
    plaintext_numbers = text_to_numbers(plaintext)
    
    ciphertext_numbers = []
    for i in range(0, len(plaintext_numbers), size):
        block = np.array(plaintext_numbers[i:i+size])
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext_numbers.extend(encrypted_block)

    ciphertext = numbers_to_text(ciphertext_numbers)
    for pos in original_spaces:
        ciphertext = ciphertext[:pos] + ' ' + ciphertext[pos:]
    return ciphertext

# Decryption function
def hill_decrypt(ciphertext, key, size, original_length):
    original_spaces = [i for i, char in enumerate(ciphertext) if char == ' ']
    ciphertext = ciphertext.replace(' ', '')
    ciphertext = process_text(ciphertext, size)
    key_matrix = create_matrix_from_key(key, size)
    key_matrix_inv = mod_inverse(key_matrix, 26)
    ciphertext_numbers = text_to_numbers(ciphertext)
    
    decrypted_numbers = []
    for i in range(0, len(ciphertext_numbers), size):
        block = np.array(ciphertext_numbers[i:i+size])
        decrypted_block = np.dot(key_matrix_inv, block) % 26
        decrypted_numbers.extend(decrypted_block)

    decrypted_text = numbers_to_text(decrypted_numbers)
    # Remove the added padding characters 'X'
    decrypted_text = decrypted_text[:original_length].rstrip('X')
    for pos in original_spaces:
        decrypted_text = decrypted_text[:pos] + ' ' + decrypted_text[pos:]
    return decrypted_text

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


size = int(input("Enter the size of the key matrix: "))
key = input(f"Enter the key (length should be {size*size} characters): ").upper().replace(' ', '')

while True:
    print("\nMenu:")
    print("1. Encrypt using Hill Cipher")
    print("2. Decrypt using Hill Cipher")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '3':
        break
    
    filename = input("Enter the filename: ")
    content = read_file(filename).upper()
    original_length = len(content.replace(' ', ''))
    
    if choice == '1':
        encrypted_content = hill_encrypt(content, key, size)
        print("Encrypted content: " + encrypted_content)
        output_filename = input("Enter the output filename: ")
        write_file(output_filename, encrypted_content)
        print("Encryption complete. Check the file:", output_filename)
        
    elif choice == '2':
        decrypted_content = hill_decrypt(content, key, size, original_length)
        print("Decrypted content: " + decrypted_content)
        output_filename = input("Enter the output filename: ")
        write_file(output_filename, decrypted_content)
        print("Decryption complete. Check the file:", output_filename)
        
    else:
        print("Invalid choice. Please try again.")
