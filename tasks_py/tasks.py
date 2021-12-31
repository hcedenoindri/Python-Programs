# MCS 275 Spring 2021, Project 1
# Hector Cedeno Indriago
# I declare that I am the sole author of this program and
# that I followed the rules given on the quiz and the
# course syllabus.
""" This module defines the classes: Task, OneTimeTask, 
    RecurringTask, BoundedRecurringTask, 
    UnboundedRecurringTask. """

import math

class Task():
    """ Defines a class for tasks, and defines
        methods to be used for children classes. Not
        meant to be used directly. """

    def __init__(self, description):
        """ Initializes the class """
        self.description = description
        self.active = False

    def next_time( self):
        """ Returns the next time this task is to be done.
            Raises an exception in this class as it's not to
            be used directly. """
        raise Exception()
    
    def run(self):
        """ Prints the information for this task. Raises
            an exception in this class as it's not to be used
            directly. """
        raise Exception()

    def retire( self, t):
        """ Retires the task marking it as "done"
            Raises an exception in this class as it's not to
            be used directly. """
        raise Exception()


class OneTimeTask( Task):
    """ Defines a children class of Task. Represents
        a one-and-done task. """

    def __init__(self, description, t):
        """ Initializes the class """
        super().__init__(description)
        self.time = t
        self.active = True

    def __str__ (self):
        """ Handles the print() call to this class """
        return ("OneTimeTask")
    
    def next_time(self):
        """ Described in Task class. """
        if self.active is False:
            raise Exception()
        return self.time
    
    def run( self):
        """ Described in Task class. """
        if self.active is False:
            raise Exception()
        print( "run: class={} description=\"{}\" time={}".format(self, self.description, self.time))
    
    def retire( self, t):
        """ Described in Task class. """
        if self.time <= t:
            self.active = False


class RecurringTask( Task):
    """ Defines a children class of Task. Represents
        a repeating task. Not to be used directly. """

    def __init__(self, description):
        """ Initializes the class """
        super().__init__(description)
    
    def num_until( self, end):
        """ Returns the number of tasks to be done 
            before time 'end'. Raises an exception 
            as this class is not be used directly. """
        raise Exception()


class BoundedRecurringTask( RecurringTask):
    """ Defines a children class of RecurringTask.
        Represents a task that is repeated a
        finite number of times. """

    def __init__(self, description, start, gap, n):
        """ Initializes the class. """
        super().__init__(description)
        self.active = True
        self.start = start
        self.gap = gap
        self.reps = n
        self.done = 0   # Number of times the task has been done until now
    
    def __str__(self):
        """ Handles the print() call to this class. """
        return ("BoundedRecurringTask")

    def next_time(self):
        """ Described in Task class. """
        if self.active is False:
            raise Exception()
        nxt_time = self.start + self.gap*self.done
        return nxt_time
    
    def run( self):
        """ Described in Task class. """
        if self.active is False:
            raise Exception()
        nxt_time = self.start + self.gap*self.done
        print( "run: class={} description=\"{}\" time={}".format(self, self.description, nxt_time))
    
    def retire( self, t):
        """ Described in Task class. """
        if self.active is False:
            raise Exception()
        elif t < self.start:
            return None
        nxt_time = self.start + self.done*self.gap
        while nxt_time <= t:
            self.done += 1
            nxt_time += self.gap
        if self.done >= self.reps:
            self.active = False

    def num_until( self, end):
        """ Described in RecurringTask class. """
        if self.active is False:
            return 0
        nxt_time = self.start + self.gap*self.done
        done = self.done
        while nxt_time <= end:
            done += 1
            nxt_time += self.gap
        return done
    
    def num_total( self):
        """ Returns the number of times this task is
            to be repeated. """
        return self.reps - self.done

        
class UnboundedRecurringTask( RecurringTask):
    """ Defines a children task of RecurringTask.
        Represents a task that is be repeated an 
        infinite amount of times. """

    def __init__(self, description, start, gap):
        """ Initializes this class. """
        super().__init__(description)
        self.active = True
        self.start = start
        self.gap = gap
        self.done = 0
    
    def __str__(self):
        """ Handles the print() call to this class. """
        return ("UnboundedRecurringTask")

    def next_time(self):
        """ Described in Task class. """
        nxt_time = self.start + self.gap*self.done
        return nxt_time
    
    def run(self):
        """ Described in Task class. """
        nxt_time = self.start + self.gap*self.done
        print("run: class={} description=\"{}\" time={}".format( self, self.description, nxt_time))

    def retire( self, t):
        """ Described in Task class. """
        if self.active is False:
            raise Exception()
        elif t < self.start:
            return None
        nxt_time = self.start + self.done*self.gap
        while nxt_time <= t:
            self.done += 1
            nxt_time += self.gap
    
    def num_until(self, end):
        """ Described in RecurringTask class. """
        if self.active is False:
            return 0
        nxt_time = self.start + self.gap*self.done
        done = self.done
        while nxt_time <= end:
            done += 1
            nxt_time += self.gap
        return done
