# =============================================================================
# Write a function named avoids that takes a word and a string of 
# forbidden letters, and that 
# returns True if the word doesn’t use any of the forbidden letters.
# =============================================================================

def avoids(word, forbidden_letters):
    avoid_letters = ''
    for l in forbidden_letters:
        if l not in avoid_letters:
            avoid_letters += l

    for ch in word:
        if ch in avoid_letters:
            return False
    return True

forbidden_letters = input('Please enter your forbidden letters\n')

fin = open('C:\\Users\\Euler\\Desktop\\words.txt')
while True:
    word = fin.readline().strip()
    if len(word) < 1:
        break
    elif avoids(word, forbidden_letters):
        print(word)

fin.close()