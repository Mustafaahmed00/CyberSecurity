def rail_fence_encrypt(text, num_rails):
    rails = [''] * num_rails
    rail = 0
    var = 1  # variable to control direction

    for char in text:
        rails[rail] += char
        rail += var
        if rail == 0 or rail == num_rails - 1:
            var = -var

    return ''.join(rails)

def rail_fence_decrypt(ciphertext, num_rails):
    length = len(ciphertext)
    rails = [[] for _ in range(num_rails)]
    rail = 0
    var = 1

    for i in range(length):
        rails[rail].append(None)
        rail += var
        if rail == 0 or rail == num_rails - 1:
            var = -var

    index = 0
    for rail in range(num_rails):
        for i in range(len(rails[rail])):
            rails[rail][i] = ciphertext[index]
            index += 1

    result = []
    rail = 0
    var = 1
    for _ in range(length):
        result.append(rails[rail].pop(0))
        rail += var
        if rail == 0 or rail == num_rails - 1:
            var = -var

    return ''.join(result)

def main_rail_fence():
    operation = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    if operation not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
        return
    text = input("Enter your text: ")
    num_rails = int(input("Enter the number of rails: "))
    if operation == 'e':
        result = rail_fence_encrypt(text, num_rails)
    else:
        result = rail_fence_decrypt(text, num_rails)
    print("Result:", result)

# Run the function
main_rail_fence()
