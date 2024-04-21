def generate_key_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # Remove duplicates from the key and convert to uppercase
    key = "".join(sorted(set(key), key=key.index)).upper()
    key += "".join([ch for ch in alphabet if ch not in key])
    # Create the matrix
    matrix = [key[i:i+5] for i in range(0, 25, 5)]
    return matrix

def preprocess_text(text):
    # Remove non-alphabet characters and convert to uppercase
    text = "".join([ch.upper() for ch in text if ch.isalpha()])
    # Replace 'J' with 'I'
    text = text.replace("J", "I")
    # Make pairs, adding X if needed to complete a pair or to separate duplicates
    pairs = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] != text[i+1]:
            pairs.append(text[i:i+2])
            i += 2
        else:
            pairs.append(text[i] + 'X')
            i += 1
    if len(pairs[-1]) < 2:
        pairs[-1] += 'X'
    return pairs

def find_position(letter, matrix):
    for i, row in enumerate(matrix):
        if letter in row:
            return i, row.index(letter)
    return None

def playfair_encrypt(pairs, matrix):
    encrypted_text = ""
    for first, second in pairs:
        row1, col1 = find_position(first, matrix)
        row2, col2 = find_position(second, matrix)
        
        if row1 == row2:
            # Same row: shift right
            encrypted_text += matrix[row1][(col1 + 1) % 5]
            encrypted_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            # Same column: shift down
            encrypted_text += matrix[(row1 + 1) % 5][col1]
            encrypted_text += matrix[(row2 + 1) % 5][col2]
        else:
            # Rectangle: swap columns
            encrypted_text += matrix[row1][col2]
            encrypted_text += matrix[row2][col1]
    return encrypted_text

def playfair_decrypt(pairs, matrix):
    decrypted_text = ""
    for first, second in pairs:
        row1, col1 = find_position(first, matrix)
        row2, col2 = find_position(second, matrix)
        
        if row1 == row2:
            # Same row: shift left
            decrypted_text += matrix[row1][(col1 - 1) % 5]
            decrypted_text += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            # Same column: shift up
            decrypted_text += matrix[(row1 - 1) % 5][col1]
            decrypted_text += matrix[(row2 - 1) % 5][col2]
        else:
            # Rectangle: swap columns
            decrypted_text += matrix[row1][col2]
            decrypted_text += matrix[row2][col1]
    return decrypted_text

def main_playfair():
    key = input("Enter the key for the Playfair cipher: ")
    operation = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    text = input("Enter the text: ")
    matrix = generate_key_matrix(key)
    pairs = preprocess_text(text)
    
    if operation == 'e':
        result = playfair_encrypt(pairs, matrix)
    else:
        result = playfair_decrypt(pairs, matrix)
    print("Result:", result)

# Run the Playfair cipher function
main_playfair()

