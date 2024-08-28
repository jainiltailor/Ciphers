J_list = []
X_list = []
length = 0

def create_key_matrix(key):
    # Normalize the key by replacing 'J' with 'I'
    key = key.upper().replace('J', 'I')  
    seen = set()
    matrix = []
    
    # Add unique characters from the key to the matrix
    for char in key:
        if char not in seen and char.isalpha(): 
            seen.add(char)
            matrix.append(char)
    
    # Add remaining alphabets to the matrix (excluding 'J')
    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    
    # Convert the list to a 5x5 matrix
    key_matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]
    return key_matrix

def J_positions(content, mode):
    J_index = []
    if mode == 1:
        for index, char in enumerate(content):
            if char == "J":
                J_index.append(index)
    return J_index

def replace_char(original_str, index, new_char):
    new_str = original_str[:index] + new_char + original_str[index + 1:]
    return new_str

def remove_char(original_str, index):
    new_str = original_str[:index] + original_str[index + 1:]
    return new_str

def PlayFair(content, key_matrix, mode):
    global X_list
    global J_list
    global length
    result = []
    content_list = []
    i = 0
    if mode == 1:
        length = len(content)
    # getting idex of J's
    if mode == 1:
        J_list = J_positions(content, mode)
    print(J_list)
    # replacing J to I for key_matrix
    content = content.replace('J','I')
    
    X_count = 0
    # Preparing the content into bigraphs
    while i < len(content):
        if i + 1 < len(content):
            if content[i] == content[i + 1]:
                pair = [content[i], 'X']
                X_list.append(i+1)
                X_count+=1
                i += 1
            else:
                pair = [content[i], content[i + 1]]
                i += 2
        else:
            pair = [content[i], 'X']
            i += 1
        content_list.append(pair)
    
    # Finding indices of each letter in the key matrix
    indices = []
    for sublist in content_list:
        sub_indices = []
        for letter in sublist:
            for i, row in enumerate(key_matrix):
                if letter in row:
                    sub_indices.append((i, row.index(letter)))
                    break
        indices.append(sub_indices)
    
    
    # Encrypting the content based on the PlayFair rules
    for small_list in indices:
        if small_list[0][0] == small_list[1][0]:
            # Same row
            result.append(key_matrix[small_list[0][0]][(small_list[0][1] + (1 if mode == 1 else -1)) % 5])
            result.append(key_matrix[small_list[1][0]][(small_list[1][1] + (1 if mode == 1 else -1)) % 5])
        elif small_list[0][1] == small_list[1][1]:
            # Same column
            result.append(key_matrix[(small_list[0][0] + (1 if mode == 1 else -1)) % 5][small_list[0][1]])
            result.append(key_matrix[(small_list[1][0] + (1 if mode == 1 else -1)) % 5][small_list[1][1]])
        else:
            # Rectangle swap
            result.append(key_matrix[small_list[0][0]][small_list[1][1]])
            result.append(key_matrix[small_list[1][0]][small_list[0][1]])
    
    result_str = ''.join(result)
    
    #Again replacing I to the J as it was in Actual Content
    if mode == 2:
        for digit in J_list:
            result_str = replace_char(result_str, digit, 'J')   
             
    # Removing X's from bi-graphs    
    if mode == 2:
        for digit in X_list:
            result_str = remove_char(result_str, digit)
    
    return result_str

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

key_matrix = create_key_matrix(key=input("Enter Key : "))
print(key_matrix)

while True:
    print("\nMenu:")
    print("1. Encrypt using Playfair Cipher")
    print("2. Decrypt using Playfair Cipher")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '3':
        break
    
    filename = input("Enter the filename: ")
    content = read_file(filename).upper()
    
    if choice == '1':
        encrypted_content = PlayFair(content,key_matrix,choice)
        output_filename = input("Enter the output filename: ")
        write_file(output_filename, encrypted_content)
        print("Encryption complete. Check the file:", output_filename)
        
    elif choice == '2':
        decrypted_content = PlayFair(content, key_matrix, choice)
        output_filename = input("Enter the output filename: ")
        write_file(output_filename, decrypted_content)
        print("Decryption complete. Check the file:", output_filename)
        
    else:
        print("Invalid choice. Please try again.")