# =============================================================================
# Write a program that reads words.txt and prints only the words with 
# more than 20 characters (not counting whitespace).
# =============================================================================

fin = open('C:\\Users\\Euler\\Desktop\\words.txt')
while True:
    a = fin.readline().strip()
    if len(a) > 20:
        print(a)
    elif len(a) < 1:
        break
fin.close()