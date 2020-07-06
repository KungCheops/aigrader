from GDPvsLE import *
import random
QUARTILES = [0.25, 0.5, 0.75]


def get_quartile(l, quartile_index):
    """ 
        Helper method to grab the correct value for a quartile.

        a) For even lists grab floor the quartile_index and take the average between the floor and the next value
        b) For uneven list then the floored quartile_index and quartile_index is the same. Just take that value 
    """
    lower_bound_index = int(quartile_index)
    lower_elem = l[lower_bound_index]
    if lower_bound_index == quartile_index:
        return l[lower_bound_index]
    else:
        upper_elem = l[lower_bound_index + 1]
        return (lower_elem + upper_elem) / 2


def quartiles(l):
    if not l:
        return None, None, None
    l.sort()
    length = len(l) - 1
    return tuple([get_quartile(l, quartile_procent * length) for
        quartile_procent in QUARTILES])


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
    random_list = [1, 1, 2, 2, 2, 3, 3, 4, 4]
    random.shuffle(random_list)
    assert quartiles(random_list) == (2.0, 2.0, 3.0)
    assert quartiles(list(range(0, 11))) == (2.5, 5.0, 7.5)
    assert quartiles(list(range(0, 101))) == (25.0, 50.0, 75.0)
    assert quartiles(list(range(-50, 51))) == (-25, 0, 25.0)
    assert quartiles([1]) == (1, 1, 1)
    print(quartiles(le))
    print(quartiles(gdp))
