"""
Practice Problem: Mumbling
from codewars.com

This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

# My solution
def accum(s):
    string = ""
    count = 0
    
    for character in s:
        string += character.upper()
        string += (count * character.lower())
        
        if count < len(s) - 1:
            string += "-"
            
        count += 1
    
    return string