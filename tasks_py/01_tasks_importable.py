"""Test that the tasks module can be imported"""
# MCS 275 Spring 2021 - David Dumas
# Part of the Project 1 starter pack

print("Trying to import the tasks module.")

try:
    import tasks
    print("Importing the module `tasks` succeeded.")
except Exception as e:
    print("ERROR: Attempting to import the `tasks` module failed.")
    print("The exception was:",e)
    exit(1)
