"""Test that the tasks module defines the required names"""
# MCS 275 Spring 2021 - David Dumas
# Part of the Project 1 starter pack

print("Trying to import the required classes from the `tasks` module.")

import tasks

required_names = [
    "Task",
    "OneTimeTask",
    "RecurringTask",
    "BoundedRecurringTask",
    "UnboundedRecurringTask"
]

for name in required_names:
    if name in dir(tasks):
        print("OK: name {} exists in module `tasks`".format(name))
    else:
        print("ERROR: name {} not found in module `tasks`".format(name))
        exit(1)