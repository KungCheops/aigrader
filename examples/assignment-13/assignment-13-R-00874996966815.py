import numpy as np
import random


def probCover(K, m, k, n):
    if k < K:
        return 0.0
    nr_successes = 0.0
    for i in range(n):
        classes = [0] * K
        for i in range(k):
            x = np.random.randint(0, K)
            classes[x] = 1
        if sum(classes) == len(classes):
            nr_successes = nr_successes + 1
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
