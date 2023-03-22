"""
AUTHOR: Mary Grizelle Hamor
DESCRIPTION: This program can encrypt a text into its Rot(n) equivalent or decrypt it through brute force.
"""

class Rot_Cipher:
    def __init__(self):
        self.dict = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

    def encrypt_rot(self, input, number):
        encoded = ""

        for character in input:
            if character.isalpha():
                for key, value in self.dict.items():
                    if character == value:
                        shift = key + number
                        if shift > 26:
                            shift -= 26
                            encoded += self.dict[shift]
                        else:
                            encoded += self.dict[shift]
            else:
                encoded += character

        print(f"\nEncoded value: \"{encoded}\"")

    # Brute force decryption
    # Checks out all possible answers by shifting it back by 1 up until 26 
    def decrypt_rot(self, input):
        decoded = ""

        print("\nDecoding...")
        for i in range(1, 27):
            for character in input:
                if character.isalpha():
                    for key, value in self.dict.items():
                        if character == value:
                            shift = key - i
                            if shift <= 0:
                                shift += 26
                                decoded += self.dict[shift]
                            else:
                                decoded += self.dict[shift]
                else:
                    decoded += character
            
            print(f"Rot({i}): {decoded}")
            decoded = ""

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
            cipher = Rot_Cipher()
            
            if action == 0:
                number = int(input("Enter a number used to shift: "))
                Rot_Cipher.encrypt_rot(cipher, text, number)
            else:
                Rot_Cipher.decrypt_rot(cipher, text)
            break
        