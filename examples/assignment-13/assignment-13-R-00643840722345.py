import numpy as np


def probCover(K, m, k, n):
    nr_successes = 0.0
    sample = np.arange(n)
    classes = [sample[i:i + m] for i in range(0, K * m, m)]
    centroids = np.random.choice(n, k)
    if k < K:
        nr_successes = 0
    else:
        for i in classes:
            for j in i:
                if j in centroids:
                    nr_successes = nr_successes + 1
        print(nr_successes)
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
