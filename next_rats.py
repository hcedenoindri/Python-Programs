# MCS 275 Spring 2021, Quiz 2, Problem 4
# Hector Cedeno Indriago
# I declare that I have used code from the Worksheet 2 solutions as a
# starting point for this program, and developed all of the additional code
# contained in this program myself. I followed the rules in the course syllabus.

""" This file contains a program that computes 
    the RATS sequence for integers 1-100 """ 

def reverse_int(n):
    """Reverse the digits of integer n and return
    the resulting integer"""
    n_str = str(n)
    # Note: int() drops leading zeros automatically, so
    # e.g. int("0012") returns 12
    return int(n_str[::-1])

def next_rats(n):
    '''Reverses, adds, then sorts an integer n'''
    sum_int = n + reverse_int(n)
    sum_digits = list(str(sum_int)) # list of digits as characters; use a list so we can sort
    sum_digits.sort() 
    # Note: sorted order of "0",...,"9" is same as that of 0,...,9, so it is OK to sort
    # the digits as a list of characters instead of a list of ints!
    sorted_sum_str = "".join(sum_digits) # join characters into a single string
    return int(sorted_sum_str)

i = 1
while i <= 100:
    max_generations = 150
    start_n = i
    rats_list = [start_n]
    n = start_n
    periodic = False
    for _ in range(max_generations):  # Conventional to use _ as name of a variable that is never used
        n = next_rats(n)
        if n in rats_list:
            print("{}: Ends at periodic sequence {}".format(start_n, rats_list[rats_list.index(n):]))
            periodic = True
            break
        else:
            rats_list.append(n)

    if not periodic:
        print("{}: No periodic sequence found in {} iterations".format (start_n, max_generations))
    i += 1