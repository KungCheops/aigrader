import numpy as np


def probCover(K, m, k, n):
    nr_successes = 0.0
    for _ in range(0, n):
        x = [False] * K
        r = np.random.randint(K * m, size=k)
        for i in range(0, k):
            x = [(x[j] or m * j < r[i] < m * (j + 1)) for j in range(0, K)]
            if all(c for c in x):
                nr_successes += 1
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
    print('Done')
