class VigenereCipher:
    def __init__(self):
        self.LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __crypt(self, mode, message, keyword):
        translated = []
        keyword_index = 0
        keyword = keyword.upper()

        for symbol in message.upper():
            num = self.LETTERS.find(symbol)
            if num != -1:  # Symbol is a letter in LETTERS
                if mode == 'encrypt':
                    num += self.LETTERS.find(keyword[keyword_index])
                elif mode == 'decrypt':
                    num -= self.LETTERS.find(keyword[keyword_index])

                num %= len(self.LETTERS)  # Handle wrap-around

                translated.append(self.LETTERS[num])

                keyword_index += 1
                if keyword_index == len(keyword):
                    keyword_index = 0
            else:
                translated.append(symbol)

        return ''.join(translated)

    def encrypt(self, message, keyword):
        return self.__crypt('encrypt', message, keyword)

    def decrypt(self, message, keyword):
        return self.__crypt('decrypt', message, keyword)

if __name__ == '__main__':
    cipher = VigenereCipher()
    action = input("Do you want to 'ENCRYPT' or 'DECRYPT'?: ").strip().lower()
    if action in ['encrypt', 'decrypt']:
        msg = input("Enter your message: ")
        key = input("Enter the keyword: ")
        if action == 'encrypt':
            print("Encrypted message:", cipher.encrypt(msg, key))
        else:
            print("Decrypted message:", cipher.decrypt(msg, key))
