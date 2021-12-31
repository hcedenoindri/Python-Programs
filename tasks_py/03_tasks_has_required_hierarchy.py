"""Test that the tasks module has the right inheritance relations"""
# MCS 275 Spring 2021 - David Dumas
# Part of the Project 1 starter pack

# This test program uses constructions not taught in MCS 275.
# It is provided to help you debug your code, not as a sample
# of something you are expected to be able to write.

print("Testing inheritance relations between classes in module `tasks`.")

import tasks

parents = {
    tasks.RecurringTask: tasks.Task,
    tasks.OneTimeTask: tasks.Task,
    tasks.BoundedRecurringTask: tasks.RecurringTask,
    tasks.UnboundedRecurringTask: tasks.RecurringTask,
}

for subclass,superclass in parents.items():
    if superclass in subclass.__bases__:
        print("OK: class {} inherits from {}".format(subclass.__name__,superclass.__name__))
    else:
        print("ERROR: class {} does not inherit from {}".format(subclass.__name__,superclass.__name__))
        exit(1)