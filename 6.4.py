# =============================================================================
# A number, a, is a power of b if it is divisible by b and a/b is a power of b.
# Write a function called is_power that takes parameters a and b and 
# returns True if a is a power of b. 
# Note:you will have to think about the base case.
# =============================================================================

def is_power(a, b):
    if a % b != 0:
        return False
    else:
        if a != b:
            return is_power(a/b, b)
    return True
    
print(is_power(8, 2))
print(is_power(128, 2))
print(is_power(3125, 5))
print(is_power(3120, 5))
print(is_power(7, 7))
print(is_power(1, 1))
