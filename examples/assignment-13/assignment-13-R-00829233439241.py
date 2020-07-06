import numpy as np


def probCover(K, m, k, n):
    nr_successes = 0.0
    total = K * m
    cntr = [False] * K
    list = [0] * n
    count = 0
    for l in range(n):
        cntr = [False] * K
        for i in range(k):
            r = 0
            r = np.random.randint(total)
            for j in range(K):
                if j * m <= r < (j + 1) * m:
                    if cntr[j] == False:
                        cntr[j] = True
        count = 0
        for s in range(K):
            if cntr[s] == True:
                count += 1
        list[l] = count
        if list[l] == K:
            nr_successes += 1
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
