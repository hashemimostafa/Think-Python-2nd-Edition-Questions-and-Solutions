# =============================================================================
# In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that
# does not contain the letter “e”. Since “e” is the most common letter
# in English, that’s not easy to do.
# In fact, it is difficult to construct a solitary thought without using that
# most common symbol. It is slow going at first, but with caution and hours of
# training you can gradually gain facility.
# All right, I’ll stop now. Write a function called has_no_e that returns True
# if the given word doesn’t have the letter “e” in it.
# Modify your program from the previous section to print only the words 
# that have no “e” and compute the percentage of the words in the list 
# that have no “e”.
# =============================================================================

def has_no_e(s):
    for ch in s:
        if ch in 'Ee':
            return False
    return True

fin = open('C:\\Users\\Euler\\Desktop\\words.txt')

total_word = 0
no_e_word = 0

while True:
    a = fin.readline().strip()
    total_word += 1
    if len(a) < 1:
        break
    if has_no_e(a):
        no_e_word += 1

print("Total words' number is:", total_word, '\nWords without e are:', no_e_word, "\nPercentage:", no_e_word/total_word * 100)
    
fin.close()