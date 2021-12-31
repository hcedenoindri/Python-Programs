# MCS 275 Spring 2021, Quiz 7
# Hector Cedeno Indriago
# I declare that I am the sole author of this program
# (except for the docstring in lumpsort), and
# that I followed the rules given on the quiz and the
# course syllabus.
""" This file contains the functions merge_sorted_lists, 
    and lumpsort. """


def merge_sorted_lists(A,B,S):
    """ Accepts 2 sorted lists A and B, and an empty
        list. A and B must be sorted in decreasing 
        order. Returns the merging of A and B into S. """
    A.reverse()
    B.reverse()
    a_pop = A.pop()
    b_pop = B.pop()
    
    if len(A) == 0 and len(B) == 0:
        if a_pop <= b_pop:
            S.append(a_pop)
            S.append(b_pop)
        else:
            S.append(b_pop)
            S.append(a_pop)
        return S

    while len(A) > 0 and len(B) > 0:
        if a_pop <= b_pop:
            S.append(a_pop)
            a_pop = A.pop()
        else:
            S.append(b_pop)
            b_pop = B.pop()

    if len(A) == 0:
        while len(B) > 0:
            if a_pop <= b_pop:
                S.append(a_pop)
                S.append(b_pop)
                while B:
                    S.append(B.pop())
                break
            else:
                S.append(b_pop)
                b_pop = B.pop()
                if len(B) == 0:
                    if a_pop <= b_pop:
                        S.append(a_pop)
                        S.append(b_pop)
                    else:
                        S.append(b_pop)
                        S.append(a_pop)
    elif len(B) == 0:
        while len(A) > 0:
            if b_pop <= a_pop:
                S.append(b_pop)
                S.append(a_pop)
                while A:
                    S.append( A.pop())
                break
            else:
                S.append(a_pop)
                a_pop = A.pop()
                if len(A) == 0:
                    if a_pop <= b_pop:
                        S.append(a_pop)
                        S.append(b_pop)
                    else:
                        S.append(b_pop)
                        S.append(a_pop)
    return S

def lumpsort(L, shortsort, shortmax):
    """Sort a list using the lumpsort algorithm.  Arguments:
    `L` : The list to be sorted.  Modified in place.
    `shortsort` : A function that accepts a single argument, a list,
                  and sorts it in place.  The list must have length
                  at most `shortmax`.
    `shortmax` : A positive integer that is the longest length of 
                 list that `shortsort` can handle."""

    length = len(L)
    if len(L) <= 0:
        raise ValueError()
    if length <= shortmax:
        return shortsort(L)
    
    lump_i = 0
    if length%2 == 0:
        lump_i = length//2 
    else:
        lump_i = (length+1)//2 
    S = L.copy()
    L.clear()
    lump1 = S[0:lump_i]
    lump2 = S[(lump_i):]
    lump1 = lumpsort(lump1, shortsort, shortmax)
    lump2 = lumpsort(lump2, shortsort, shortmax)

    return merge_sorted_lists(lump1, lump2, L)
    