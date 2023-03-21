"""
AUTHOR: Mary Grizelle Hamor
DESCRIPTION: This program is a palindrome checker that lets the user enter a word and determine if its a palindrome or not.
"""

def main():
    string = input("Enter a word: ")

    new_string = clean_string(string)
    print(f"\"{string}\"" + palindrome_checker(new_string))

def clean_string(string):
    new_string = ""

    # ensure the string is in lowercase
    string = string.lower()

    # removes spaces in the 
    string.strip()

    # removes non-alphanumeric characters
    if string.isalpha() == False:
        for character in string:
            if character.isalpha():
                new_string += character
        return new_string
    else:
        return string

def palindrome_checker(string):
    # find the reversed version of the string
    reverse_string = ""
    for character in string:
        reverse_string = character + reverse_string
    
    # determine if the string is a palindrome
    if reverse_string == string:
        return " is A Palindrome"
    else:
        return " is NOT a Palindrome"

if __name__ == "__main__":
    main() 


