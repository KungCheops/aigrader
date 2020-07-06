import numpy as np


def probCover(K, m, k, n):
    nr_successes = 0.0
    for i in range(n):
        class_count = [0] * K
        dp = np.ones((m, K))
        for j in range(k):
            res = 1
            while not res == 0:
                cent_K = np.random.randint(0, K)
                cent_m = np.random.randint(0, m)
                if not dp[cent_m, cent_K] == 0:
                    dp[cent_m, cent_K] == 0
                    class_count[cent_K] += 1
                    res = res - 1
        if not 0 in class_count:
            nr_successes += 1
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed(3)
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
