from itertools import islice
from itertools import izip_longest as zip_longest
def sublist(s_list):
    l_list = []
    for i, j in zip_longest(s_list, islice(s_list, 1, None), fillvalue=s_list[-1]):
        l_list.append(i)
        if i > j:
            yield l_list
            l_list = []
    yield l_list
def longest_common_list(s_list):
    org_slist = sublist(s_list)
    rev_slist = sublist(s_list[::-1])
    long_clist = max([i for i in org_slist and rev_slist], key = len)
    return long_clist
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]