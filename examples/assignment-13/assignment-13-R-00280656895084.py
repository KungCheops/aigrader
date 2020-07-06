import numpy as np
import random


def probCover(K, m, k, n):
    nr_successes = 0.0
    max_value = K * m - 1
    for _ in range(n):
        cover = {int(centroid / m) for centroid in np.random.randint(
            max_value, size=(k, 1))}
        if len(cover) == K:
            nr_successes += 1
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
    assert probCover(4, 1, 100, 1) > 0.98
