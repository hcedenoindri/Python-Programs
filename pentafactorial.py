# MCS 275 Spring 2021, Project 1
# Hector Cedeno Indriago
# I declare that I am the sole author of this program and
# that I followed the rules given on the quiz and the
# course syllabus.
""" This file contains the function pentafactorial(n) """

def pentafactorial(n, flag = True):
    """Accepts n as a required arg and flag as an optional
       arg. Returns the pentafactorial of n. """ 
    if (n < 5 and flag):
        return 1
    elif (n <= 5):
        return n
    return n*pentafactorial(n-5, flag=False)