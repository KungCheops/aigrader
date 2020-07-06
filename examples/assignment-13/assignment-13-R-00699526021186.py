import numpy as np


def probCover(K, m, k, n):
    nr_successes = 0.0
    for trial in range(n):
        clusters = np.zeros([K, m])
        for sample in range(k):
            clusters[np.random.randint(0, K), np.random.randint(0, m)] = 1
        has_any_zero_row = True
        for row in range(K):
            if 1 not in clusters[row]:
                has_any_zero_row = False
        if has_any_zero_row:
            nr_successes += 1
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
