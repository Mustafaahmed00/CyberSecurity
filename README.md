Classic Cipher Suite

This repository contains Python implementations of five classic ciphers: Caesar, Vigenère, Rail Fence, Atbash, and Playfair. Each cipher offers a unique method of encryption, providing a fascinating glimpse into the history and evolution of cryptographic techniques.

Ciphers Overview
1. Caesar Cipher

How It Works: The Caesar Cipher is a substitution cipher that encrypts text by shifting each letter in the plaintext a fixed number of positions down the alphabet. For example, with a shift of 1, 'A' becomes 'B', 'B' becomes 'C', and so on. The same shift is used to decrypt the message by shifting in the opposite direction.

2. Vigenère Cipher

How It Works: The Vigenère Cipher uses a keyword to determine the shift for each letter in the plaintext. The keyword is repeated or truncated as necessary to match the length of the plaintext. Each letter of the plaintext is shifted forward in the alphabet by a number of positions equal to the position of the corresponding keyword letter in the alphabet.

3. Rail Fence Cipher

How It Works: The Rail Fence Cipher involves writing the message in a zigzag pattern over a set number of rows (rails), and then reading off each row in order to create the ciphertext. For decryption, the process is reversed, requiring knowledge of the number of rails used.

4. Atbash Cipher

How It Works: The Atbash Cipher is a monoalphabetic substitution cipher that replaces each letter in the plaintext with the corresponding letter from the reversed alphabet. Thus, 'A' is replaced by 'Z', 'B' by 'Y', and so on. This cipher is its own inverse, meaning the same operation is used to both encrypt and decrypt.

5. Playfair Cipher

How It Works: The Playfair Cipher uses a 5x5 matrix of letters, constructed from a keyword. Pairs of letters in the plaintext are encoded together. If the letters of a pair appear in the same row of the matrix, each is replaced by the letter to its right (wrapping around to the start of the row if needed). If the letters appear in the same column, each is replaced by the letter beneath it (again, wrapping to the top if necessary). If the letters are not aligned in a row or column, each letter is replaced by the letter in the same row but in the column of the other letter of the pair.

Significance of These Ciphers

These ciphers represent important steps in the development of cryptographic techniques. From simple shift ciphers like the Caesar Cipher to more complex polyalphabetic ciphers like the Vigenère Cipher, each has contributed to the field of cryptography in different historical contexts. The Playfair Cipher, introduced in the 19th century, marked a significant advancement in making cryptography more practical and difficult to crack without a key.

Project Structure

Each cipher is implemented in a separate Python file:

caesar_cipher.py
vigenere_cipher.py
rail_fence_cipher.py
atbash_cipher.py
playfair_cipher.py

Usage

Each file is a standalone script that can be run from the terminal. Users will be prompted to enter the text and select whether they wish to encrypt or decrypt. Specific ciphers, like the Vigenère and Playfair, also require a key.

Contributing

Contributions to this project are welcome. Feel free to fork the repository, make changes, and submit a pull request. If you find any bugs or have suggestions for additional features, please open an issue.
