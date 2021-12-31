def common_chars(s1,s2):
    """Return a set of all characters that are present in both
    strings `s1` and `s2`."""
    common = set()
    c1 = set(s1)
    c2 = set(s2)
    for c in c1:
        if c in c2:
            common.add(c)
    return common

if __name__=="__main__":
    import random
import time

s1 = ''.join([ random.choice(["edfghijklmnopqrstuvwxyzzzzzzzzzzzzzzzz"]) for _ in range(50000) ])
s2 = ''.join([ random.choice(["abcedfghijklmnopqrstuvw"]) for _ in range(50000) ]) + 'z'

t_start = time.time()
both = common_chars(s1,s2)
t_end = time.time()

print("Common characters:")
print(both)
print("\nRunning time: {:.2f} seconds".format(t_end-t_start))
