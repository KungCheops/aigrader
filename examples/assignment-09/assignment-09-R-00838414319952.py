from GDPvsLE import *
import logging
logging.basicConfig(level=logging.INFO)


def quartiles(l):
    Q1 = 0
    Q2 = 0
    Q3 = 0
    if l is None or len(l) == 0:
        return Q1, Q2, Q3
    l.sort()
    list_size = len(l)
    is_list_even_size = list_size % 2 == 0
    if is_list_even_size:
        q1_list = l[:len(l) / 2]
        Q1 = find_median_of_list(q1_list)
        Q2 = find_median_of_list(l)
        q3_list = l[len(l) / 2:]
        Q3 = find_median_of_list(q3_list)
    else:
        index_of_middle_value = int(list_size / 2)
        q1_list = l[:index_of_middle_value + 1]
        Q1 = find_median_of_list(q1_list)
        Q2 = find_median_of_list(l)
        q3_list = l[index_of_middle_value:]
        Q3 = find_median_of_list(q3_list)
    logging.debug('>> List = ' + str(l))
    logging.debug('>> Q1 List = ' + str(q1_list))
    logging.info('>> Q1 = ' + str(Q1))
    logging.info('>> Q2 = ' + str(Q2))
    logging.debug('>> Q3 List = ' + str(q3_list))
    logging.info('>> Q3 = ' + str(Q3))
    return Q1, Q2, Q3


def find_median_of_list(l):
    list_size = len(l)
    is_list_even_size = list_size % 2 == 0
    if is_list_even_size:
        index_value1 = int(list_size / 2 - 1)
        index_value2 = int(index_value1 + 1)
        median = int((l[index_value1] + l[index_value2]) / 2)
        return median
    else:
        index_of_middle_value = int(list_size / 2)
        return l[index_of_middle_value]


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
