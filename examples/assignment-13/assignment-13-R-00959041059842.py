import numpy as np
import random


def probCover(K, m, k, n):
    nr_successes = 0.0
    classes = {y for y in range(1, K + 1)}
    for i in range(n):
        centroids = [random.randrange(1, K + 1) for i in range(k)]
        classes_with_centroids = [value for value in classes if value in
            centroids]
        if len(classes_with_centroids) == K:
            nr_successes += 1
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
