# =============================================================================
# Fermat’s Last Theorem says that there are no positive integers a, b, and c 
# such that a^n + b^n = c^n
# for any values of n greater than 2.
# 1. Write a function named check_fermat that takes four parameters
# —a, b, c and n— and checks to see if Fermat’s theorem holds. If n is 
# greater than 2 and a^n + b^n = c^n
# the program should print, “Holy smokes, Fermat was wrong!” 
# Otherwise the program should print, “No, that doesn’t work.”
# 2. Write a function that prompts the user to input values for a, b, c and n,
# converts them to integers, and uses check_fermat 
# to check whether they violate Fermat’s theorem.
# =============================================================================

def check_fermat(a, b, c, n):
    Fermat_condition = a**n + b**n - c**n
    if Fermat_condition == 0 and n > 2:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn’t work.')
        
print('Checking Fermat’s Last Theorem\n')
a = input('Please enter a\n')
b = input('Please enter b\n')
c = input('Please enter c\n')
n = input('Please enter n\n')

check_fermat(int(a), int(b), int(c), int(n))