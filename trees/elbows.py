# MCS 275 Spring 2021, Quiz 7
# Hector Cedeno Indriago
# I declare that I am the sole author of this program and
# that I followed the rules given on the quiz and the
# course syllabus.
""" This file contains the functions is_elbow(x)
    and elbow_count(x). """

from binary import Node

def is_elbow(x):
    """ Accepts a Node x and returns a True if
    x is an elbow. """
    if x is None:
        return False
    if (x.right is None) ^ (x.left is None):
        return True
    return False

def elbow_count(x):
    """ Accepts a binary tree with root Node x and 
    returns the number of elbows in the tree. """
    if x is None:
        return 0
    if (x.right is None) and (x.left is None):
        return 0
    if is_elbow(x) is True:
        return 1 + elbow_count(x.right) + elbow_count(x.left)
    return elbow_count(x.right) + elbow_count(x.left)
