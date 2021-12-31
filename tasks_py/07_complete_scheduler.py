"""Make a bunch of tasks, keep them in a queue, and run them"""
# MCS 275 Spring 2021 - David Dumas
# Part of the Project 1 starter pack

import tasks

# ------------------------------------------------------------
# The part of this program between the two horizontal lines
# is only here to allow comparison between the actual output
# and the expected output.
expected_output_lines = """run: class=UnboundedRecurringTask description="C" time=2
run: class=BoundedRecurringTask description="B" time=3
run: class=OneTimeTask description="A" time=5
status: previous task is finished, not returning it to the queue
run: class=BoundedRecurringTask description="B" time=6
run: class=UnboundedRecurringTask description="C" time=7
run: class=BoundedRecurringTask description="B" time=9
run: class=BoundedRecurringTask description="B" time=12
run: class=UnboundedRecurringTask description="C" time=12
run: class=BoundedRecurringTask description="B" time=15
status: previous task is finished, not returning it to the queue
run: class=UnboundedRecurringTask description="C" time=17
status: exiting because 10 tasks have run""".splitlines()
expected_output_lines.reverse()

def expected():
    try:
        line = expected_output_lines.pop()
    except IndexError:
        line = ""
    print("\nE: {}\nA: ".format(line),end="")   

print("This script prints pairs of lines.")
print("In each pair, the first is the EXPECTED output, prefixed with E:")
print("The next is the ACTUAL output obtained using your code, prefixed with A:")
print("These should match exactly if your module behaves as required.")
# ------------------------------------------------------------


# The actual task scheduling work begins here.
queue = []
queue.append(tasks.OneTimeTask("A",t=5))
queue.append(tasks.BoundedRecurringTask("B",start=3,gap=3,n=5))
queue.append(tasks.UnboundedRecurringTask("C",start=2,gap=5))

# This example includes an unbounded task, so it will run
# forever if we don't impose a limit.  For this script we
# only simulate a total of `EXIT_AFTER` task executions.
EXIT_AFTER = 10

n = 0 # tasks run so far
while queue:
    # Next step is needlessly inefficient: It sorts the entire
    # list in order of decreasing run time, but after the first
    # iteration, only the last element could possibly be in the
    # wrong position.  Later we'll learn a more efficient way
    # to handle this.
    queue.sort(key = lambda x:x.next_time(),reverse=True)
    task = queue.pop() # Task with earliest run time
    runtime = task.next_time() # When it needs to be run
    # Instead of waiting for the run time to arrive, we
    # just pretend that moment has arrived.
    expected() # show expected output line
    task.run() # run the task (which prints a line of output)
    task.retire(runtime) # retire it
    if task.active:
        # The task needs to run again.  Put it in the queue.
        queue.append(task)
    else:
        # The task is complete.  It doesn't need to go back in the queue.
        expected() # show the expected output line
        print("status: previous task is finished, not returning it to the queue")
    n += 1
    if n == EXIT_AFTER:
        break
    
expected() # show the expected output line
print("status: exiting because {} tasks have run".format(EXIT_AFTER))