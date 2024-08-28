def vigenere_cipher(text, key, mode):
    out_text = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    text_int = [ord(i) for i in text]
    value=0
    j = 0  # Key index tracker
    for i in range(len(text_int)):
        if text[i].isalpha():  # Encrypt / Decrypt only alphabetic characters
            if mode==1: # Encryption
                value = (text_int[i] + key_as_int[j % key_length] - 2 * ord('A')) % 26
            elif mode==2: # Decryption
                value = (text_int[i] - key_as_int[j % key_length] + 26) % 26
            out_text.append(chr(value + ord('A')))            
            j += 1
        else:
            out_text.append(text[i])  # Preserve spaces and punctuation
    
    return ''.join(out_text)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


key = input(f"Enter the key: ").upper().replace(' ', '')

while True:
    print("\nMenu:")
    print("1. Encrypt using Vigenere Cipher")
    print("2. Decrypt using Vigenere Cipher")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 3:
        break
    
    filename = input("Enter the filename: ")
    content = read_file(filename).upper()    
    if choice == 1:
        encrypted_content = vigenere_cipher(content, key,choice)
        print("Encrypted content: " + encrypted_content)
        output_filename = input("Enter the output filename: ")
        write_file(output_filename, encrypted_content)
        print("Encryption complete. Check the file:", output_filename)
        
    elif choice == 2:
        decrypted_content = vigenere_cipher(content, key, choice)
        print("Decrypted content: " + decrypted_content)
        output_filename = input("Enter the output filename: ")
        write_file(output_filename, decrypted_content)
        print("Decryption complete. Check the file:", output_filename)
        
    else:
        print("Invalid choice. Please try again.")

