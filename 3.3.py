# =============================================================================
# Note: This exercise should be done using only the statements and 
# other features we have learned so far.
# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:
# print('+', '-')
# 
# By default, print advances to the next line, but you can override 
# that behavior and put a space at the end, like this:
# print('+', end=' ')
# print('-')
# 
# The output of these statements is '+ -' on the same line. The output from 
# the next print statement would begin on the next line.
# 2. Write a function that draws a similar grid with four rows and 
# four columns. Solution: http://thinkpython2.com/code/grid.py . 
# Credit: This exercise is based on an exercise in Oualline, 
# Practical C Programming, Third Edition, O’Reilly Media, 1997.
# =============================================================================

filled_line = '+' + 4*'-' + '+' + 4*'-' + '+'
empty_line =  '|' + 4*' ' + '|' + 4*' ' + '|'
print(filled_line)
print(empty_line)
print(empty_line)
print(empty_line)
print(empty_line)
print(filled_line)
print(empty_line)
print(empty_line)
print(empty_line)
print(empty_line)
print(filled_line)

def grid(n):
    print('=' * (n+1) * n)
    filled_line = '+'
    empty_line =  '|' 

    for i in range(n):
        filled_line += n*'-' + '+'
        empty_line +=  n*' ' + '|' 

    print(filled_line)
    for i in range(n):
        for j in range(n):
            print(empty_line)
        print(filled_line)

grid(4)