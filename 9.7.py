# =============================================================================
# This question is based on a Puzzler that was broadcast on the radio program 
# Car Talk (http://www.cartalk.com/content/puzzlers ):
# Give me a word with three consecutive double letters. I’ll give you 
# a couple of words that almost qualify, but don’t. For example, 
# the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ 
# that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could 
# take out those i’s it would work. But there is a word that has three
# consecutive pairs of letters and to the best of my knowledge this may be 
# the only word. Of course there are probably 500 more but I can only 
# think of one. What is the word? Write a program to find it. 
# Solution: http://thinkpython2.com/code/cartalk1.py .
# =============================================================================

def have_3_double_letters(word):
    if len(word) < 6:
        return False
    
    co_word = word
    for i in range(26):
        double = 2 * chr(97 + i)
        co_word = co_word.replace(double, '')

    count = (len(word) - len(co_word)) / 2  
    if count > 2:
        return True
    else:
        return False
     
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if have_3_double_letters(word):
        for i in range(len(word)-5):
            cond1 = word[i] == word[i+1]
            cond2 = word[i+2] == word[i+3]
            cond3 = word[i+4] == word[i+5]
            if cond1 and cond2 and cond3:
                print(word)