# =============================================================================
# Write a function named uses_only that takes a word and a string of letters, 
# and that returns True if the word contains only letters in the list. 
# Can you make a sentence using only
# the letters acefhlo? Other than “Hoe alfalfa?”
# =============================================================================

def uses_only(word, letter):
    for w in word:
        if w not in letter:
            return False
    return True

def checker(fin, string):
    fin.seek(0)
    li = []
    for line in fin:
        word = line.strip()
        if uses_only(word, string):
            li.append(word)
    return li

fin = open('C:\\Users\\Euler\\Desktop\\words.txt')
string1 = 'acefhlo'
string2 = 'Hoe alfalfa'

print(string1, '\n', checker(fin, string1))
print('\n', string2, '\n', checker(fin, string2))

fin.close()