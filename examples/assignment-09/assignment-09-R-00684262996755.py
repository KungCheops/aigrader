from GDPvsLE import gdp


def find_median(l):
    """
    This function takes a sorted list of values and returns the median value.
    """
    n = int(len(l) / 2)
    if len(l) % 2 == 0:
        median = (l[n - 1] + l[n]) / 2
    else:
        median = l[n]
    return median


def quartiles(l):
    """
    This function takes a list, sort it and returns the value of the 1st, 
    2nd and 3rd quartile.
    """
    ls = sorted(l)
    Q2 = find_median(ls)
    n = int(len(l) / 2)
    if len(ls) % 2 == 0:
        ls_lower = ls[:n]
        ls_upper = ls[n:]
        Q1 = find_median(ls_lower)
        Q3 = find_median(ls_upper)
    else:
        ls_lower = ls[:n + 1]
        ls_upper = ls[n:]
        Q1 = find_median(ls_lower)
        Q3 = find_median(ls_upper)
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
    assert quartiles([1, 8, 2, 7, 3, 6, 4, 5]) == (2.5, 4.5, 6.5)
    assert quartiles([1, 7, 2, 6, 3, 5, 4]) == (2.5, 4.0, 5.5)
    assert quartiles([1, 6, 2, 5, 3, 4]) == (2.0, 3.5, 5.0)
    Q1, Q2, Q3 = quartiles(gdp)
    print(Q1, Q2, Q3)
