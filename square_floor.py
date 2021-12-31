# MCS 275 Spring 2021, Quiz 2, Problem 2
# Hector Cedeno Indriago
# I declare that I am the sole author of this program and
# that I followed the rules given on the quiz and the
# course syllabus.

""" This file contains the function: square_floor """

def square_floor (n):
    """ Takes an integer n as argument and
        returns the largest perfect square that
        is less than or equal to n """
    i = 0
    square = 0
    while square < n:
        i += 1
        square = i**2
    if square > n:
       i -= 1
       square = i**2
    return square