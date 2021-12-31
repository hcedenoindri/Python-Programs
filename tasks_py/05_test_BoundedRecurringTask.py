"""Test some behavior of BoundedRecurringTask"""
# MCS 275 Spring 2021 - David Dumas
# Part of the Project 1 starter pack

import tasks

print("This script prints pairs of lines.")
print("In each pair, the first is the EXPECTED output, prefixed with E:")
print("The next is the ACTUAL output obtained using your code, prefixed with A:")
print("These should match exactly if your module behaves as required.")

e = tasks.BoundedRecurringTask("Lead MCS 275 discussion",start=16432,gap=40,n=15)
print("\nE: 16432\nA: ",end="")
print(e.next_time())  # prints 16432

print("\nE: 15\nA: ",end="")
print(e.num_total())  # prints 15

print("\nE: 2\nA: ",end="")
print(e.num_until(16500)) # prints 2, for the actions at 16432 and 16472

e.retire(100) # does nothing; there are no actions at or before time t=100

print("\nE: run: class=BoundedRecurringTask description=\"Lead MCS 275 discussion\" time=16432\nA: ",end="")
e.run() # prints: 'run: class=BoundedRecurringTask description="Lead MCS 275 discussion" time=16432'

e.retire(16432) # retires the task run on the previous line (marks it done)

print("\nE: 16472\nA: ", end="")
print(e.next_time()) # prints 16472

print("\nE: 14\nA: ",end="")
print(e.num_total())  # prints 14, since one of the originally scheduled instances has been retired
