class Caesar:
    def __init__(self):
        self.LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.translated = ''

    def __crypt(self, mode, message, key):
        for symbol in message.upper():
            if symbol in self.LETTERS:
                num = self.LETTERS.find(symbol)
                if mode == 'encrypt':
                    num = num + key
                elif mode == 'decrypt':
                    num = num - key

                if num >= len(self.LETTERS):
                    num -= len(self.LETTERS)
                elif num < 0:
                    num += len(self.LETTERS)

                self.translated += self.LETTERS[num]
            else:
                self.translated += symbol

        return self.translated

    def encrypt(self, message, key):
        self.translated = ''
        return self.__crypt('encrypt', message, key)

    def decrypt(self, message, key):
        self.translated = ''
        return self.__crypt('decrypt', message, key)

if __name__ == '__main__':
    cipher = Caesar()
    while True:
        action = input("Do you want to 'ENCRYPT' or 'DECRYPT' or 'EXIT'?: ").strip().lower()
        if action == 'exit':
            break
        elif action in ['encrypt', 'decrypt']:
            msg = input("Enter your message: ")
            key = int(input("Enter the key (1-25): "))
            if action == 'encrypt':
                print("Encrypted message:", cipher.encrypt(msg, key))
            elif action == 'decrypt':
                print("Decrypted message:", cipher.decrypt(msg, key))
        else:
            print("Invalid command, please choose 'ENCRYPT', 'DECRYPT', or 'EXIT'.")

