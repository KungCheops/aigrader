import numpy as np


def probCover(K, m, k, n):
    nr_successes = 0.0
    choices = []
    occurrences = [0] * K
    if k >= K:
        for j in range(n):
            for i in range(k):
                choices.append(np.random.randint(K * m))
            for c in choices:
                if occurrences[int(c / m)] == 0:
                    occurrences[int(c / m)] += 1
            if sum(occurrences) == K:
                nr_successes += 1
            occurrences = [0] * K
            del choices[:]
    return nr_successes / n


if __name__ == '__main__':
    np.random.seed(12)
    print('k\tProb hitting all classes')
    for k in range(3, 21):
        print('%d\t%1.3f' % (k, probCover(4, 100, k, 10000)))
    assert probCover(4, 100, 3, 1000) == 0.0
    assert 0.05 < probCover(4, 100, 4, 1000) < 0.15
