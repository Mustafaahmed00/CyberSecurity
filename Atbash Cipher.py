def atbash_cipher(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reversed_alphabet = alphabet[::-1]
    cipher = ''
    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            cipher += reversed_alphabet[index]
        else:
            cipher += char  # keeping punctuation and spaces unchanged
    return cipher

def main_atbash():
    operation = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    if operation not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
        return
    text = input("Enter your text: ")
    result = atbash_cipher(text)
    print("Result:", result)

# Run the function
main_atbash()
