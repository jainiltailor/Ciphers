# Caesar Cipher Program

## Overview

This is a simple Python program that implements the Caesar Cipher for text encryption and decryption. The program reads text from a file, applies the Caesar Cipher algorithm to either encrypt or decrypt the text based on a user-provided shift value, and then writes the result to a new file.

## Features

- **Encrypt Text**: Reads text from a file (`sender.txt`), encrypts it using the Caesar Cipher with a specified shift value, and writes the encrypted text to `encrypted.txt`.
- **Decrypt Text**: Reads encrypted text from `encrypted.txt`, decrypts it using the Caesar Cipher with the same shift value, and writes the decrypted text to `decrypted.txt`.
- **User-Friendly Interface**: The program provides a simple menu-based interface for users to select their desired operation.

## Files

- `sender.txt`: The file from which the original text is read for encryption.
- `encrypted.txt`: The file where the encrypted text is saved.
- `decrypted.txt`: The file where the decrypted text is saved.

## How to Use

1. **Clone the Repository**
   ```
   git clone https://github.com/jainiltailor/caesar-cipher-program.git
   cd caesar-cipher-program
   ```

2. **Prepare the Input File**
   - Place the text you want to encrypt in the `sender.txt` file.

3. **Run the Program**
   - Execute the script using Python:
     ```
     python caesar_cipher.py
     ```

4. **Select an Option**
   - Choose between encryption and decryption from the menu:
     - Option 1: Encrypt the text.
     - Option 2: Decrypt the text.

5. **Enter the Shift Value**
   - Input the shift value when prompted. The same value should be used for both encryption and decryption.

6. **Check the Output Files**
   - After encryption, the encrypted text will be saved in `encrypted.txt`.
   - After decryption, the decrypted text will be saved in `decrypted.txt`.

## Example

- **Original Text (`sender.txt`)**: `Hello, World!`
- **Shift Value**: `3`
- **Encrypted Text (`encrypted.txt`)**: `Khoor, Zruog!`
- **Decrypted Text (`decrypted.txt`)**: `Hello, World!`

## Requirements

- Python 3.x

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.
