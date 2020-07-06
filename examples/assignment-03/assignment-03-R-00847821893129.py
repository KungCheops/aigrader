from collections import Counter
def sublist(s_list):
    sublist = []
    for e in s_list:
        if not sublist or e >= sublist[-1]:
            sublist += [e]
        else:
            if len(sublist) > 1:
                yield sublist
            sublist = [e]
    yield sublist
def longest_common_list(s_list):
    non_rev_sublists = list(sublist(s_list))
    rev_sublists = list(sublist([e for e in reversed(s_list)]))
    sublists = non_rev_sublists + rev_sublists
    most_common = list(Counter(tuple(e) for e in sublists).most_common(1)[0][0])
    return most_common
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]