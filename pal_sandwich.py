# MCS 275 Spring 2021
# Hector Cedeno Indriago
# I declare that I am the sole author of this program and
# that I followed the rules given on the quiz and the
# course syllabus.

def is_palindrome_sandwich(s):
    length = len(s)
    if length < 5:
        return False
    if length%2 == 0:
        return False
    if length == 5:
        if s[0] == s[-1]:
            return True
        else:
            return False
    
    return s[0] == s[-1] and is_palindrome_sandwich( s[1:-1])

def palindrome_multisandwich(s):
    length = len(s)
    b_index = ((length - 3)//2)
    a = s[0:b_index]
    if is_palindrome_sandwich(s):
        return 1+palindrome_multisandwich(a)
    else:
        return 0

