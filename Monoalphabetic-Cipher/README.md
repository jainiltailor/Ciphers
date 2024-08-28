# Monoalphabetic Cipher Program

## Overview

This Python program implements the Monoalphabetic Cipher for encrypting and decrypting text. In a Monoalphabetic Cipher, each letter in the plaintext is substituted with another letter from the alphabet. The substitution is consistent throughout the text, making it a simple yet secure encryption method.

## Features

- **Encrypt Text**: Encrypts the text read from a file using a randomly generated Monoalphabetic Cipher key and saves the encrypted text to a specified output file.
- **Decrypt Text**: Decrypts the text read from a file using a provided Monoalphabetic Cipher key and saves the decrypted text to a specified output file.
- **Key Generation**: Automatically generates a random substitution key for encryption.

## Files

- `input.txt`: The file from which the original text is read for encryption or decryption.
- `output.txt`: The file where the encrypted or decrypted text is saved.

## How to Use

1. **Clone the Repository**
   ```
   git clone https://github.com/jainiltailor/Ciphers/Monoalphabetic-Cipher.git
   cd Ciphers/Monoalphabetic-Cipher
   ```

2. **Prepare the Input File**
   - Place the text you want to encrypt or decrypt in the `input.txt` file.

3. **Run the Program**
   - Execute the script using Python:
     ```
     python monoalphabetic_cipher.py
     ```

4. **Select an Option**
   - Choose between encryption and decryption from the menu:
     - Option 1: Encrypt the text.
     - Option 2: Decrypt the text.
     - Option 3: Exit the program.

5. **Provide Filenames**
   - Specify the filename for the input text (e.g., `input.txt`) and the output filename for the encrypted or decrypted text.

6. **Encryption Process**
   - If you choose encryption, a random key will be generated, which will be displayed on the screen. Save this key securely, as you will need it for decryption.
   - The encrypted text will be saved in the specified output file.

7. **Decryption Process**
   - If you choose decryption, you will need to input the key used during encryption.
   - The decrypted text will be saved in the specified output file.

## Example

- **Original Text (`input.txt`)**: `Hello World`
- **Generated Key**: `QWERTYUIOPLKJHGFDSAZXCVBNM`
- **Encrypted Text (`output.txt`)**: `Itssg Vgksr`
- **Decrypted Text (`output.txt`)**: `Hello World`

## Requirements

- Python 3.x

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.
