import numpy as np


def probCover(K, m, k, n):
    nr_successes = 0.0
    list = [0] * n
    nr_dataPoints = K * m
    for i in range(n):
        counter = [False] * K
        for j in range(k):
            rn = np.random.randint(nr_dataPoints)
            for c in range(K):
                if c * m <= rn < (c + 1) * m:
                    if counter[c] == False:
                        counter[c] = True
            count = 0
            for c in range(K):
                if counter[c] == True:
                    count += 1
            list[j] = count
            if list[j] == K:
                nr_successes += 1
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
