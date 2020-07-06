import numpy as np
import random


def probCover(K, m, k, n):
    nr_successes = 0.0
    if m <= 0 or K <= 0 or k <= 0 or n <= 0:
        return None
    if k < K:
        return 0
    if k >= K:
        elem = {i: (i % K) for i in range(K * m)}
        for i in range(n):
            x = random.sample(list(elem), k)
            if {elem[i] for i in x} == set(range(K)):
                nr_successes += 1
        return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
