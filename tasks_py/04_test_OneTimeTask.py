"""Test some behavior of OneTimeTask"""
# MCS 275 Spring 2021 - David Dumas
# Part of the Project 1 starter pack

import tasks

print("This script prints pairs of lines.")
print("In each pair, the first is the EXPECTED output, prefixed with E:")
print("The next is the ACTUAL output obtained using your code, prefixed with A:")
print("These should match exactly if your module behaves as required.")

e = tasks.OneTimeTask("Receive Nobel Prize",t=1981823) # create a one-time Task object
print("\nE: 1981823\nA: ",end="")
print(e.next_time())  # prints 1981823
e.retire(100) # does nothing; it is not scheduled to run at or before time t=100
print("\nE: run: class=OneTimeTask description=\"Receive Nobel Prize\" time=1981823\nA: ",end="")
e.run() # prints the following: 'run: class=OneTimeTask description="Receive Nobel Prize" time=1981823'
e.retire(1981823) # retires the task
print("\nE: <exception raised>")
try:
    print("A: ",end="")
    print(e.next_time()) # raises exception, because the task is no longer active
except Exception as e:
    print("<exception raised>")
