import numpy as np
import random


def probCover(K, m, k, n):
    nr_successes = 0.0
    for x in range(n):
        rand_list = set()
        for i in range(k):
            rand_list.add(np.random.randint(1, K + 1))
        for j in range(1, K + 1):
            if j not in rand_list:
                break
            if j is K and j in rand_list:
                nr_successes += 1
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 10, 3, 100) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
