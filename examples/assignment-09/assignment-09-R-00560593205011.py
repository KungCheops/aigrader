from GDPvsLE import *


def quartiles(l):
    l.sort()
    if len(l) % 2 == 0:
        median = (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
        if len(l) % 4 == 0:
            q1 = (l[int(len(l) * 0.25)] + l[int(len(l) * 0.25) - 1]) / 2
            q3 = (l[int(len(l) * 0.75)] + l[int(len(l) * 0.75 - 1)]) / 2
        else:
            q1 = l[int(len(l) * 0.25)]
            q3 = l[int(len(l) * 0.75)]
        print(q1, median, q3)
    else:
        median = l[len(l) // 2]
        if len(l[0:median]) % 2 == 0:
            q1 = (l[int(len(l) * 0.25)] + l[int(len(l) * 0.25) + 1]) / 2
            q3 = (l[int(len(l) * 0.75)] + l[int(len(l) * 0.75 - 1)]) / 2
        else:
            q1 = l[int(len(l) * 0.25)]
            q3 = l[int(len(l) * 0.75)]
    return q1, median, q3


print(quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
    18, 19, 20]))
if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
