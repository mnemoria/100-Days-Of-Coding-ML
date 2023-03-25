"""
Practice Problem: WeIrD StRiNg CaSe
from codewars.com

Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').
"""

# My solution
def to_weird_case(words):
    count = 0
    new_string = ""
    
    word_list = []
    
    for word in words.split():
        for character in word:
            if count == 0 or count % 2 == 0:
                new_string += character.upper()
            else:
                new_string += character.lower()
            count += 1
        
        word_list.append(new_string)
        new_string = ""
        
        count = 0
        
    return " ".join(word_list)