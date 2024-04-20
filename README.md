Classical Cipher Implementations

This repository contains Python implementations of two historical encryption algorithms: the Caesar cipher and the Vigenère cipher. These ciphers represent early methods of cryptology and provide an educational insight into the evolution of encryption techniques.

Overview

Caesar Cipher

The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down the alphabet. For example, with a shift of 1, 'A' would be replaced by 'B', 'B' would become 'C', and so on. This repository includes a Python implementation that allows the user to encrypt and decrypt messages using a specified shift key.

Vigenère Cipher

The Vigenère cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. Unlike the Caesar cipher, which shifts all letters by the same number throughout the entire message, the Vigenère cipher uses a keyword to determine the shift for each letter. This makes it significantly more secure against simple frequency analysis. This repository provides a Python implementation to encrypt and decrypt using a provided keyword.

Functions

Caesar Cipher Functions

Encrypt: Shifts the plaintext by a specified key to produce ciphertext.

Decrypt: Reverses the shift applied by the encryption key to return the original text.

Vigenère Cipher Functions

Encrypt: Uses a keyword to vary the shift applied to each letter, encrypting the plaintext into ciphertext.

Decrypt: Applies the reverse shift using the same keyword to decrypt the ciphertext back to plaintext.

Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.
