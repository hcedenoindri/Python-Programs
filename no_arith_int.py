# MCS 275 Spring 2021, Quiz 2, Problem 4
# Hector Cedeno Indriago
# I declare that I have used code from the Worksheet 2 solutions 
# as a starting point for this program, and developed all 
# of the additional code contained in this program myself. 
# I also followed the rules in the course syllabus.
""" This file declares defines a subclass of int
    called NoArithInt, which forbids arithmetic 
    operations to be done on it. """

class NoArithInt(int):
    """ subclass of int that forbids arithmetic operations """
    def __init__(self, value):
        super().__init__()
        self.value = value
    
    def __add__(self, other):
        raise TypeError ("unsupported operand type(s) for +: 'NoArithInt' and 'NoArithInt'")

    def __sub__(self, other):
        raise TypeError ("unsupported operand type(s) for -: 'NoArithInt' and 'NoArithInt'")
    
    def __mul__(self, other):
        raise TypeError ("unsupported operand type(s) for *: 'NoArithInt' and 'NoArithInt'")

    def __truediv__(self, other):
        raise TypeError ("unsupported operand type(s) for /: 'NoArithInt' and 'NoArithInt'")

