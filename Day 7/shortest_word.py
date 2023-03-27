"""
Practice Problem: Mumbling
from codewars.com

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

# My solution #1 [using a list]
def find_short(s):
    s = s.split()
    min_length = len(s[-1])
    
    for word in s:
        if len(word) < min_length:
            min_length = len(word)
        
    return min_length

# My solution #2 [without using a list]
def find_short(s):
    start = 0
    count = 1
    min_length = 0
    
    string = ""
    
    for character in s + " ":
        if character == " ":
            if start == 0:
                min_length = len(string)
                start += 1

            if min_length > len(string):
                min_length = len(string)
            
            string = ""
        else:
            string += character
        
        count += 1
        
    return min_length 