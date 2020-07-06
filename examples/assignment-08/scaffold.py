# Scaffold for solution to DIT 852, Programming task 1
#
from GDPvsLE import *

def sum(l):
    # Example: Compute a sum of values
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values
    

def stats(l):
    # Compute summary statistics for a list
    # Insert your code for part 1 below

    return sum_values, min_value, max_value, avg_value


def histogram(l):
    # Compute summary statistics for a list
    # Insert your code for part 2 below

    
    # Here bin_count should be a list with ten entries corresponding to counts
    # in each bin
    return bin_count
   
# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert sum([1,2,3,4,5]) ==  15
    assert stats([1,2,3,4,5]) == (15,1,5,3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]

    
