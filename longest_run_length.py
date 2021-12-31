# MCS 275 Spring 2021, Quiz 2, Problem 3
# Hector Cedeno Indriago
# I declare that I have used code from the Worksheet 2 solutions as a
# starting point for this program, and developed all of the additional code
# contained in this program myself. I followed the rules in the course syllabus.

""" This file contains the function: longest_run_length """

def longest_run_length (text):
    """ Returns an integer count of the maximum 
        repeated letters from the input text """
    count = [0] 
    consecutive_duplicates = 1
    previous_char = ""

    for c in text:
        if c == previous_char:
            consecutive_duplicates += 1
        else:
            if consecutive_duplicates > 1:
                count.append (consecutive_duplicates)
                consecutive_duplicates = 1
        previous_char = c
   
    if consecutive_duplicates > 1:
        count.append (consecutive_duplicates)

    x = max(count)
    if text != "" and x==0:
        x = 1
    return x