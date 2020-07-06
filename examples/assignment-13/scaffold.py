# Scaffold for solution to DIT 852, Programming task 6
#
import numpy as np

def probCover(K, m, k, n):
    # Given K, the number of classes, m the number of data points per
    # class, k, the number of centroids (and thus clusters in k-means)
    # and n, the number of samples, as input, compute the probability
    # that at least one centroid per class was chosen, when randomly
    # selecting data points as centroids.
    nr_successes = 0.0


    
    return nr_successes / n
    

    
# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    np.random.seed() # Initialize random number generator
    print("k\tProb hitting all classes")
    for k in range(3,21):
        print("%d\t%1.3f"% (k, probCover(4, 100, k, 10000)))
        
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
    


    
