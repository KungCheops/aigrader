from math import inf
def sublist(s_list):
    my_sublist = []
    prev_s = inf
    for s in range(len(s_list)):
        new_s = s_list[s]
        if new_s < prev_s:
            my_sublist = []
        my_sublist.append(new_s)
        yield my_sublist
        prev_s = new_s
def longest_common_list(s_list):
    rev_list = [s_list[-i] for i in range(1, len(s_list)+1)]
    gen_fwd = sublist(s_list)
    sublists_fwd = [next(gen_fwd) for _ in range(len(s_list))]
    sublists_fwd = set(tuple(row) for row in sublists_fwd)
    gen_rev = sublist(rev_list)
    sublists_rev = [next(gen_rev) for _ in range(len(s_list))]
    sublists_rev = set(tuple(row) for row in sublists_rev)
    intersection = sublists_fwd.intersection(sublists_rev)
    is_as_list = list(intersection)
    result = max(is_as_list, key=len)
    return list(result)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]