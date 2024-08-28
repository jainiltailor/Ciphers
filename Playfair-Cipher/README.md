# Playfair Cipher Program

## Overview

This Python program implements the Playfair Cipher for encrypting and decrypting text. The Playfair Cipher is a digraph substitution cipher that encrypts pairs of letters instead of single letters, providing a more secure encryption method than simple substitution ciphers.

## Features

- **Encrypt Text**: Encrypts the text read from a file using the Playfair Cipher and a user-provided key. The encrypted text is saved to a specified output file.
- **Decrypt Text**: Decrypts the text read from a file using the Playfair Cipher and a user-provided key. The decrypted text is saved to a specified output file.
- **Handling of Special Cases**: The program handles specific cases, such as replacing 'J' with 'I' during encryption and preserving the original content structure (e.g., spaces and special characters) during decryption.

## Files

- `input.txt`: The file from which the original text is read for encryption or decryption.
- `output.txt`: The file where the encrypted or decrypted text is saved.

## How to Use

1. **Clone the Repository**
   ```
   git clone https://github.com/jainiltailor/Ciphers/Playfair-Cipher.git
   cd Ciphers/Playfair-Cipher
   ```

2. **Prepare the Input File**
   - Place the text you want to encrypt or decrypt in the `input.txt` file.

3. **Run the Program**
   - Execute the script using Python:
     ```
     python playfair_cipher.py
     ```

4. **Select an Option**
   - Choose between encryption and decryption from the menu:
     - Option 1: Encrypt the text.
     - Option 2: Decrypt the text.
     - Option 3: Exit the program.

5. **Provide Filenames**
   - Specify the filename for the input text (e.g., `input.txt`) and the output filename for the encrypted or decrypted text.

6. **Encryption Process**
   - If you choose encryption, you will be prompted to enter a key. The key will be used to generate a 5x5 key matrix for the Playfair Cipher.
   - The encrypted text will be saved in the specified output file.

7. **Decryption Process**
   - If you choose decryption, you will be prompted to enter the same key used during encryption.
   - The decrypted text will be saved in the specified output file.

## Example

- **Original Text (`input.txt`)**: `HELLO WORLD`
- **Key**: `MONARCHY`
- **Encrypted Text (`output.txt`)**: `IBSUPGAYLK`
- **Decrypted Text (`output.txt`)**: `HELXLOXWORLD`

## Requirements

- Python 3.x

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.
