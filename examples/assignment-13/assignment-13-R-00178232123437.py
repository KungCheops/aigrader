import numpy as np


def probCover(K, m, k, n):
    if K > k or n < 1:
        return 0.0
    nr_successes = 0.0
    for _ in range(n):
        class_centroids = set()
        centroids = np.random.randint(K * m, size=k)
        for c in centroids:
            for i in range(1, k + 1):
                if c < m * i and c > m * (i - 1):
                    class_centroids.add(i)
        if len(class_centroids) >= K:
            nr_successes += 1
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
