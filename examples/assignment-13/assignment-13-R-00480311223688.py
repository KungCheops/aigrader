import numpy as np
import random


def probCover(K, m, k, n):
    nr_successes = 0.0
    s = 0
    centroids = []
    data = []
    while s < K:
        for i in range(0, m):
            data.append(s)
        s = s + 1
    counter_list = [0] * K
    trials = n
    while trials > 0:
        for i in range(0, k):
            centroids.append(random.choice(data))
        for c in centroids:
            counter_list[c] = counter_list[c] + 1
        if 0 not in counter_list:
            nr_successes = nr_successes + 1
        centroids = []
        counter_list = [0] * K
        trials = trials - 1
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
