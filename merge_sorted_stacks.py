def merge_sorted_stacks(A,B,S):
    a_pop = A.pop()
    b_pop = B.pop()
    
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
                for _ in B:
                    S.append(B.pop())
                break
            else:
                S.append(b_pop)
                b_pop = B.pop()

        if a_pop <= b_pop:
            S.append(a_pop)
            S.append(b_pop)
        else:
            S.append(b_pop)
            S.append(a_pop)

    else:

        while len(A) > 0:
            if a_pop <= b_pop:
                S.append(a_pop)
                a_pop = A.pop()
            else:
                S.append(b_pop)
                for _ in A:
                    S.append( A.pop())

        if a_pop <= b_pop:
            S.append(a_pop)
            S.append(b_pop)
        else:
            S.append(b_pop)
            S.append(a_pop)       

    return S
