import numpy as np
import random


def probCover(K, m, k, n):
    nr_successes = 0.0
    for r in range(n):
        Lister = []
        for i in range(k):
            x = random.randint(1, K)
            Lister.append(x)
            Lister = list(set(Lister))
        for z in range(1, K + 1):
            if z is K:
                if z in Lister:
                    nr_successes += 1
                    break
            if z in Lister:
                continue
            else:
                break
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
