# Hill Cipher Program

## Overview

This Python program implements the Hill Cipher for encrypting and decrypting text. The Hill Cipher is a type of polygraphic substitution cipher that uses linear algebra and matrix multiplication to encrypt blocks of text.

## Features

- **Encrypt Text**: Encrypts the text read from a file using the Hill Cipher with a specified key matrix and block size, then saves the encrypted text to a specified output file.
- **Decrypt Text**: Decrypts the text read from a file using the Hill Cipher, with the same key matrix and block size, then saves the decrypted text to a specified output file.
- **Supports Space Preservation**: The program preserves spaces in the original text during encryption and decryption.

## Files

- `input.txt`: The file from which the original text is read for encryption or decryption.
- `output.txt`: The file where the encrypted or decrypted text is saved.

## How to Use

1. **Clone the Repository**
   ```
   git clone https://github.com/jainiltailor/Ciphers/Hill-Cipher.git
   cd Hill-Cipher
   ```

2. **Prepare the Input File**
   - Place the text you want to encrypt or decrypt in the `input.txt` file.

3. **Run the Program**
   - Execute the script using Python:
     ```
     python hill_cipher.py
     ```

4. **Select an Option**
   - Choose between encryption and decryption from the menu:
     - Option 1: Encrypt the text.
     - Option 2: Decrypt the text.
     - Option 3: Exit the program.

5. **Enter the Key Matrix Size**
   - Input the size of the key matrix (e.g., for a 2x2 matrix, enter `2`).

6. **Enter the Key**
   - Input the key string, ensuring the length matches the size of the key matrix (e.g., for a 2x2 matrix, the key should be 4 characters long).

7. **Provide Filenames**
   - Specify the filename for the input text (e.g., `input.txt`) and the output filename for the encrypted or decrypted text.

8. **Check the Output Files**
   - After encryption, the encrypted text will be saved in the specified output file.
   - After decryption, the decrypted text will be saved in the specified output file.

## Example

- **Original Text (`input.txt`)**: `HELLO WORLD`
- **Key Matrix Size**: `2`
- **Key**: `GYBNQKURP`
- **Encrypted Text (`output.txt`)**: `NSMMSMUOI`
- **Decrypted Text (`output.txt`)**: `HELLOWORLD`

## Requirements

- Python 3.x
- NumPy library

## Installation

To install the necessary dependencies, run:
```
pip install numpy
```

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.
