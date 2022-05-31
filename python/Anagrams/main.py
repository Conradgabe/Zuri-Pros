# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True
word = input('Enter 2 words to check if they are anagrams: ')
word2 = input('Enter another word to check: ')

def find_anagrams(word, word2):
    # [assignment] Add your code here
    if len(word) == len(word2):
        if sorted(word) == sorted(word2):
            return True
        elif sorted(word) != sorted(word2):
            return False
    else:
        return False

print(find_anagrams(word, word2))