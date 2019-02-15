# =============================================================================
# Modify your program to prompt the user to enter a string of forbidden letters
# and then print the number of words that don’t contain any of them.
# Can you find a combination of 5 forbidden letters
# that excludes the smallest number of words?
# =============================================================================
''' In case we have a redundant charecter 
we should increase number of forbidden letters to 7 instead of 5.
In the following example, "a ,e" are reptarive charachters
'''

def avoids(word, forbidden_letters):
    avoid_letters = ''
   
    for l in forbidden_letters:
        if l not in avoid_letters:
            avoid_letters += l

    for ch in word:
        if ch in avoid_letters:
            return False
    return True

def count_avoids(fin,forbidden_letters):
    fin.seek(0)
    total = 0        
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden_letters):
            total += 1
    return total

fin = open('C:\\Users\\Euler\\Desktop\\words.txt')
alphabet = [0 for i in range(26)]

for line in fin:
    word = line.strip()
    for ch in word:
        no = ord(ch) - 97
        alphabet[no] += 1
for i in range(26):
    print(chr(97 + i), alphabet[i], end = '; ')

forbidden_letters_length = 7        
forbidden_letters = [alphabet[i] for i in range(forbidden_letters_length)]
min_index = 0

for i in range(len(alphabet)):
    for j in range(len(forbidden_letters)):
        if forbidden_letters[j] < forbidden_letters[min_index]:
            min_index = j
    if alphabet[i] > forbidden_letters[min_index]:
        forbidden_letters[min_index] = alphabet[i]

best_forbidden_letters = ''

for j in forbidden_letters:
    for i in range(len(alphabet)):
        condition1 = alphabet[i] == j
#        condition2 = chr(97 + i) not in best_forbidden_letters
        if condition1:
            best_forbidden_letters += chr(97 + i)         

print('\n\nThe most redundant letters are:', best_forbidden_letters)      
print('Number of occurance: ', count_avoids(fin, best_forbidden_letters))

fin.close()