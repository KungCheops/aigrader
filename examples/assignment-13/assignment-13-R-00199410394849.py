import numpy as np
import random as rd


def probCover(K, m, k, n):
    nr_successes = 0.0
    KM = K + 1
    sample = np.arange(n)
    arr = [sample[i:i + m] for i in range(0, K * m, m)]
    for i in range(n):
        tmp = []
        centroids = 0
        for j in range(k):
            centroids = rd.randint(1, K)
            tmp.append(centroids)
            tmp = list(set(tmp))
        for a in range(1, KM):
            if a is K and a in tmp:
                nr_successes += 1
                break
            if a in tmp:
                continue
            else:
                break
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
