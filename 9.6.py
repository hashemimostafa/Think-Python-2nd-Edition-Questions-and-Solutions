# =============================================================================
# Write a function called is_abecedarian that returns True if the letters
# in a word appear in alphabetical order (double letters are ok). 
# How many abecedarian words are there?
# =============================================================================

def is_abecedarian(word):
    for i in range(len(word)-1):
        if ord(word[i]) > ord(word[i+1]):
            return False
    return True

fin = open('words.txt')
li = []

for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        li.append(word)
        
print(len(li))

fin.close()