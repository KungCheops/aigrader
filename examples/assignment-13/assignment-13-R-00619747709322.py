import numpy as np


def probCover(K, m, k, n):
    nr_successes = 0.0
    c = True
    u = np.zeros((K, m))
    for i in range(n):
        for i in range(k):
            u.flat[np.random.randint(K * m)] = 1
        for i in range(K):
            if not 1 in u[i]:
                c = c and False
        if c:
            nr_successes += 1
        c = True
        u *= 0
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
