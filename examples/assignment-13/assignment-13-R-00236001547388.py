import numpy as np
import random


def probCover(K, m, k, n):
    nr_successes = 0.0
    n_class = list(range(0, K * m))

    def divide_chunks(l, n):
        random.shuffle(l)
        for i in range(0, len(l), n):
            yield l[i:i + n]
    l = m
    f_class = list(divide_chunks(n_class, l))
    if k >= K:
        for i in range(n):
            n_centlist = np.zeros(K, dtype=int)
            n_centroids = np.random.randint(0, K * m, size=k)
            for j in range(k):
                for z in range(K):
                    if n_centroids[j] in f_class[z]:
                        n_centlist[z] += 1
            if 0 not in n_centlist:
                nr_successes += 1
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
