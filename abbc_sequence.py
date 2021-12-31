# MCS 275 Spring 2021, Quiz 2, Problem 4
# Hector Cedeno Indriago
# I declare that I have used the Worksheet 6 solutions 
# as a starting point for this program, and developed all 
# of the additional code contained in this program myself. 
# I also followed the rules in the course syllabus.
""" This file contains the abbc(n) function """

def abbc(n):
    """ Takes an integer n and returns the nth iteration
        of the sequence Q_n = Q_n-1 + 2Q_n-2 + Q_n-3 """ 
    if (n < 0):
        raise Exception("Non-valid n value.")
    elif (n <= 2):
        return n
    return abbc(n-1) + 2*abbc(n-2) + abbc(n-3)
