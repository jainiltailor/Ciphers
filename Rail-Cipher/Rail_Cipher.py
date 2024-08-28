def rail_encrypt(text, length):
    matrix = []
    
    for i in range(length):
        sub = ['-' for j in range(len(text))]
        matrix.append(sub)
    
    i = 0
    j = 0
    direction_down = True
    
    for char in text:
        matrix[j][i] = char
        i += 1
        
        if direction_down:
            j += 1
            if j == length:  
                j -= 2
                direction_down = False
        else:
            j -= 1
            if j < 0:
                j += 2
                direction_down = True
    
    encrypted_text = ''
    for row in matrix:
        for char in row:
            if char != '-':
                encrypted_text += char
    
    for row in matrix:
        print(row)
        print()
    
    return encrypted_text

def rail_decrypt(encrypt, length):
    matrix = []
    
    for i in range(length):
        sub = ['-' for j in range(len(encrypt))]
        matrix.append(sub)
    
    i = 0
    j = 0
    direction_down = True
    
    for char in encrypt:
        matrix[j][i] = '*'
        i += 1
        
        if direction_down:
            j += 1
            if j == length:
                j -= 2
                direction_down = False
        else:
            j -= 1
            if j < 0:
                j += 2
                direction_down = True
    
    k = 0
    for row in range(length):
        for col in range(len(encrypt)):
            if matrix[row][col] == '*' and k < len(encrypt):
                matrix[row][col] = encrypt[k]
                k += 1
    
    decrypted_text = ''
    i = 0
    j = 0
    direction_down = True
    
    for _ in range(len(encrypt)):
        decrypted_text += matrix[j][i]
        i += 1
        
        if direction_down:
            j += 1
            if j == length:
                j -= 2
                direction_down = False
        else:
            j -= 1
            if j < 0:
                j += 2
                direction_down = True
    
    for row in matrix:
        print(row)
        print()
    
    return decrypted_text

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


key = int(input(f"Enter the Rail Length: "))

while True:
    print("\nMenu:")
    print("1. Encrypt using Rail Cipher")
    print("2. Decrypt using Rail Cipher")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 3:
        break
    
    filename = input("Enter the filename: ")
    content = read_file(filename).upper()    
    if choice == 1:
        encrypted_content = rail_encrypt(content,key)
        print("Encrypted content: " + encrypted_content)
        output_filename = input("Enter the output filename: ")
        write_file(output_filename, encrypted_content)
        print("Encryption complete. Check the file:", output_filename)
        
    elif choice == 2:
        decrypted_content = rail_decrypt(content,key)
        print("Decrypted content: " + decrypted_content)
        output_filename = input("Enter the output filename: ")
        write_file(output_filename, decrypted_content)
        print("Decryption complete. Check the file:", output_filename)
        
    else:
        print("Invalid choice. Please try again.")


plain_text = input("Enter Text: ")
rail = int(input("Rail Length: "))

encrypt = rail_encrypt(plain_text, rail)
print("Encrypted:", encrypt)

decrypt = rail_decrypt(encrypt, rail)
print("Decrypted:", decrypt)
