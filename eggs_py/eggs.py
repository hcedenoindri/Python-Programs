# MCS 275 Spring 2021, Project 1
# Hector Cedeno Indriago
# I declare that I am the sole author of this program and
# that I followed the rules given on the quiz and the
# course syllabus.
""" This file contains the functions is_egg(s), 
    is_superegg_iterative(s), is_superegg_recursive(s),
    and is_hyperegg(s). """

import math

def is_egg(s):
    """ Recieves a string s and returns True
        if s is an egg. """
    if len(s) != 3:
        return False
    if s[-2] == s[-1]:
        return True
    return False
    

def is_superegg_iterative(s):
    """ Recieves a string s and returns True
        if s is a superegg. Applies iteration. """
    if len(s) < 3 or len(s)%2 == 0:
        return False
    if s[-2] != s[-1]:
        return False
    if is_egg(s):
        return True
    
    A = s[0:-2]
    flag = True
    while( flag):
        if len(A) < 3:
            return False
        if A[-2] != A[-1]:
            return False
        if len(A) == 3:
            flag = False
        A = A[0:-2]
    return True    

def is_superegg_recursive(s):
    """ Recieves a string s and returns True
        if s is a superegg. Applies recursion. """
    if len(s) < 3 or len(s)%2 == 0:
        return False
    if s[-2] != s[-1]:
        return False
    if is_egg(s):
        return True
    return is_superegg_recursive(s[0:-2])   


def is_hyperegg(s):
    """ Accepts a string s and returns True
        if s is a hyperegg. """
    if len(s) < 3 or len(s)%2 == 0:
        return False
    if s[-2] != s[-1]:
        return False

    if is_superegg_iterative(s):
        return True
    if len(s) == 3:
        return False

    for i in range(1, len(s), 2):
        A = s[0:i]
        len_B = int((len(s)-len(A))/2)
        if len_B%2 == 0:
            continue
        s_b = len_B + i-1

        B_1 = s[(len(A)):(s_b)+1]
        B_2 = s[(s_b+1):]
        if s_b == len(A):
            B_1 = s[-1]
            B_2 = s[-2]

        if B_1 == B_2:
            if len(A) == 1:
                return is_hyperegg(B_1)
            elif len(B_1) == 1:
                return is_hyperegg(A)
            elif is_hyperegg(A) and is_hyperegg(B_1):
                return True
    return False
    

if __name__=="__main__":
    i = 0
    f = open("eggsTests/hypereggs.txt", "r")
    for line in f:
        i+=1
        if line and line[-1] == "\n":  # (`line` nonempty) and (`line` ends with "\n")
            # remove the trailing newline
            line = line[:-1]
        print(i, is_hyperegg(line))
    f.close()
