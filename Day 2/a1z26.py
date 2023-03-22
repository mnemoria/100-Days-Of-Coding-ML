"""
AUTHOR: Mary Grizelle Hamor
DESCRIPTION: This program can encrypt a text into its A1Z26 equivalent or decrypt it.
"""

class Alphanumeric_Cipher:

    # A126 is a monoalphabetic cipher where A = 1, B = 2, ..., Z = 26
    def __init__(self):
        self.dict = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

    def encrypt(self, input):
        encoded = ""

        for character in input:
            if character.isalpha():
                for key, value in self.dict.items():
                    if character == value:
                        encoded += str(key) + " "
            else:
                encoded += character

        print(f"\nEncoded value: \"{encoded}\"")

    # 
    def decrypt(self, input):
        decoded = ""

        for character in input:
            if character.isnumeric():
                for key, value in self.dict.items():
                    if int(character) == key:
                        decoded += value
            else:
                decoded += character
            
        print(f"Decoded value: \"{decoded}\"")
            

if __name__ == "__main__":
    text = input("\nEnter your text: ")
    text = text.lower()
    
    while True:
        print("\nActions:\n \
            0 : Encrypt text\n \
            1 : Decrypt text\n")

        action = int(input("Chosen action: "))

        if action > 1 or action < 0:
            print("Warning: You have chosen an invalid input.")
            continue
        else:
            cipher = Alphanumeric_Cipher()
            
            if action == 0:
                Alphanumeric_Cipher.encrypt(cipher, text)
            else:
                text_list = text.split()
                Alphanumeric_Cipher.decrypt(cipher, text_list)
            break
        