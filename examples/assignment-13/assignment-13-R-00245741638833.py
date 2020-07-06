import numpy as np


def probCover(K, m, k, n):
    nr_successes = 0.0
    successful = True
    for x in range(0, n):
        centroids = np.random.randint(low=1, high=K * m, size=k)
        for i in range(1, K + 1):
            if successful:
                successful = False
                for created_num in centroids:
                    if created_num in range(m * (i - 1) + 1, m * i):
                        successful = True
                        break
            else:
                break
        if successful:
            nr_successes += 1
        successful = True
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
