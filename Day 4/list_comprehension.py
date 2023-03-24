# Practice problems for Python's list comprehension

# Problem #1
# Print the list of words that is not an article in the English language

article = ['a', 'an', 'the']

#text = input("Enter text: ")
#text = text.lower()
#text = text.split()

#output_1 = [word for word in text if word not in article]
#print(output_1)



# Problem #2
# Print the list of all the words in the sentence. However, if a word has more than 5 characters, print it in reverse.

#text = input("Enter text: ")
text = "i am grizelle"
text = text.lower()
text = text.split()

output_2 = [word[::-1] if len(word) > 5 else word for word in text]
print(output_2)