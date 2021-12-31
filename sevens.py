# MCS 275 Spring 2021, Quiz 1, Problem2
# Hector Cedeno Indriago is the sole author
# of this Python script.
""" Checks for sevens in powers of 2"""

n = int (input ("Enter number of powers of 2 to examine: "))

i = 0
count = 0
sevens = [0]
while i < n:
    count = 0
    num = 2**i
    number = str (num)
    for ch in number:
        if ch == '7':
            count += 1

    if count > len (sevens) - 1:
        j = len (sevens) - 1
        while j < count:
            sevens.append (0)
            j += 1
    sevens[ count] += 1

    i += 1

print ("Among the first", n, "powers of 2:")
index = 0
while index < len (sevens):
    print (sevens[ index], "of them have", index, "instance(s) of the digit 7")
    index += 1
