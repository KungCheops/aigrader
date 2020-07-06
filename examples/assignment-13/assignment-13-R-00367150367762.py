import numpy as np
import random


def probCover(K, m, k, n):
    nr_successes = 0.0
    big_list = []
    for x in range(K):
        innerList = []
        for y in range(m):
            innerList.append(x)
        big_list += innerList
    s = set()
    for z in range(K):
        s.add(z)
    for i in range(n):
        p = set()
        for q in range(k):
            q = random.choice(big_list)
            p.add(q)
        if p == s:
            nr_successes += 1
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
