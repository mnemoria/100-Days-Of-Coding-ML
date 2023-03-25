"""
Practice Problem: Disemvowel Trolls
from codewars.com

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
"""

# My solution
def disemvowel(string_):
    
    new_string = ""
    
    for character in string_:
        if character.lower() not in ['a', 'e', 'i', 'o', 'u']:
            new_string += character   

    return new_string