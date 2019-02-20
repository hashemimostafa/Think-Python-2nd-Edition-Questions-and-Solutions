# =============================================================================
# Write a function named uses_all that takes a word and a string of 
# required letters, and that returns True if the word uses all 
# the required letters at least once. How many words are there that use 
# all the vowels aeiou? How about aeiouy?
# =============================================================================

def use_all(word, string):
    for letter in string:
        if letter not in word:
            return False
    return True

def checker(fin, string):
    fin.seek(0)
    li = []
    for line in fin:
        word = line.strip()
        if use_all(word, string):
            li.append(word)
    return len(li)
            
fin = open('words.txt')
string1 = 'aeiou'
string2 = 'aeiouy'

print(string1, '\t', checker(fin, string1))
print(string2, '\t', checker(fin, string2))