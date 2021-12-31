"""Test some behavior of BoundedRecurringTask"""
# MCS 275 Spring 2021 - David Dumas
# Part of the Project 1 starter pack

import tasks

print("This script prints pairs of lines.")
print("In each pair, the first is the EXPECTED output, prefixed with E:")
print("The next is the ACTUAL output obtained using your code, prefixed with A:")
print("These should match exactly if your module behaves as required.")

e = tasks.UnboundedRecurringTask("Read course evaluations",start=16100,gap=650)
print("\nE: 16100\nA: ",end="")
print(e.next_time())  # prints 1611
print("\nE: 2\nA: ",end="")
print(e.num_until(17000)) # prints 2, for the actions at 16100 and 16750
e.retire(100) # does nothing; there are no actions at or before time t=100
print("\nE: run: class=UnboundedRecurringTask description=\"Read course evaluations\" time=16100\nA: ",end="")
e.run() # prints: 'run: class=UnboundedRecurringTask description="Read course evaluations" time=16100
e.retire(16100) # retires the action scheduled for time 16100
print("\nE: 16750\nA: ",end="")
print(e.next_time()) # prints 16750
