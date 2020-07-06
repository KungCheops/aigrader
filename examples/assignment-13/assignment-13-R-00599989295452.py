import numpy as np
import random


def probabilitySample(K, m, k):
    listOfClasses = [-1] * (K * m)
    iterator = 0
    for i in range(K):
        for j in range(m):
            listOfClasses[iterator] = i + 1
            iterator += 1
    random.shuffle(listOfClasses)
    isPresent = [False] * K
    i = 0
    while isPresent.__contains__(False) and i < k:
        isPresent[listOfClasses[i] - 1] = True
        i = i + 1
    if isPresent.__contains__(False):
        return False
    else:
        return True


def probCover(K, m, k, n):
    if not K or not m or not k or not n:
        return None
    nr_successes = 0.0
    for i in range(n):
        nr_successes += probabilitySample(K, m, k)
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed()
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
