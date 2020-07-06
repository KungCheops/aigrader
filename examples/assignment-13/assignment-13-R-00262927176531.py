import numpy as np


def probCover(K, m, k, n):
    nr_successes = 0.0
    if K <= k:
        for i in range(n):
            centroid_class = np.zeros(K)
            centroid = np.random.randint(0, K * m, size=k)
            for i in range(len(centroid)):
                for j in range(K):
                    if centroid[i] in range(j * m, (j + 1) * m):
                        centroid_class[j] += 1
            if np.amin(centroid_class) > 0:
                nr_successes += 1
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
