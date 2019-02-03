# =============================================================================
# A string slice can take a third index that specifies the “step size”; that is,
# the number of spaces between successive characters. A step size of 2 means 
# every other character; 3 means every third, etc.
# >>> fruit = 'banana'
# >>> fruit[0:5:2]
# 'bnn'
# A step size of -1 goes through the word backwards, so the slice [::-1] 
# generates a reversed string.
# Use this idiom to write a one-line version of is_palindrome from Exercise 6.3.
# =============================================================================

def is_palindrome1(s):
    c = int(len(s) / 2)
    for i in range(c):
        if s[i] != s[-i-1]:
            return False
            break
    return True

def is_palindrome2(s):
    return s == s[::-1]

print(is_palindrome1('anabbbana'))
print(is_palindrome2('anbbana'))