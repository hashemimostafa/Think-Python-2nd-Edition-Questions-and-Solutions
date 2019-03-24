# =============================================================================
# Here’s another Car Talk Puzzler you can solve with a search 
# (http://www.cartalk.com/content/puzzlers):
# “Recently I had a visit with my mom and we realized that the two digits that 
# make up my age when reversed resulted in her age. For example, if she’s 73, 
# I’m 37. We wondered how often this has happened over the years but we got 
# sidetracked with other topics and we never came up with an answer.
# “When I got home I figured out that the digits of our ages have been 
# reversible six times so far. I also figured out that if we’re lucky it 
# would happen again in a few years, and if we’re really lucky it would happen 
# one more time after that. In other words, it would have happened 8 times
# over all. So the question is, how old am I now?”
# Write a Python program that searches for solutions to this Puzzler. 
# Hint: you might find the string method zfill useful.
# Solution: http://thinkpython2.com/code/cartalk3.py .
# =============================================================================

def search(diff, max_human_age):
    count = 0
    kid = 0
    mom = kid + diff
    li = []
    while mom < max_human_age:
        if str(mom) == str(kid).zfill(2)[::-1]:
            li.append((kid, mom))
            count += 1
        kid += 1
        mom = kid + diff
    return li

max_human_age = 120
max_occurrence = 8
mom = 1

while mom < max_human_age:
    diff = mom
    occurrence = search(diff, max_human_age)
    if len(occurrence) == max_occurrence:
        print(occurrence)
        print("Kid's age is: ",occurrence[5][0])
    mom += 1