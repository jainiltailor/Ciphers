# Transposition Cipher Program

## Overview

This Python program implements the Transposition Cipher, a method of encryption where the positions of the plaintext characters are shifted according to a defined key. The program supports both encryption and decryption of text using a user-defined key.

## Features

- **Encrypt Text**: Encrypts the text read from a file using the Transposition Cipher with a user-defined key. The encrypted text is saved to a specified output file.
- **Decrypt Text**: Decrypts the text read from a file using the Transposition Cipher with a user-defined key. The decrypted text is saved to a specified output file.

## Files

- `input.txt`: The file from which the original text is read for encryption or decryption.
- `output.txt`: The file where the encrypted or decrypted text is saved.

## How to Use

1. **Clone the Repository**
   ```
   git clone https://github.com/jainiltailor/Ciphers/Transposition-Cipher.git
   cd Ciphers/Transposition-Cipher
   ```

2. **Prepare the Input File**
   - Place the text you want to encrypt or decrypt in the `input.txt` file.

3. **Run the Program**
   - Execute the script using Python:
     ```
     python transposition_cipher.py
     ```

4. **Select an Option**
   - Choose between encryption and decryption from the menu:
     - Option 1: Encrypt the text.
     - Option 2: Decrypt the text.
     - Option 3: Exit the program.

5. **Provide Filenames**
   - Specify the filename for the input text (e.g., `input.txt`) and the output filename for the encrypted or decrypted text.

6. **Encryption Process**
   - If you choose encryption, you will be prompted to enter the key. The text will be rearranged according to the key, and the encrypted text will be saved in the specified output file.

7. **Decryption Process**
   - If you choose decryption, you will be prompted to enter the same key used during encryption. The text will be decrypted, and the original text will be saved in the specified output file.

## Example

- **Original Text (`input.txt`)**: `HELLO WORLD`
- **Key**: `3214`
- **Encrypted Text (`output.txt`)**: `EHLLOOLWRD`
- **Decrypted Text (`output.txt`)**: `HELLO WORLD`

## Requirements

- Python 3.x

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.
