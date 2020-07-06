def sublist(s_list):
    yield []
    subseq_start = 0
    for i in range(subseq_start, len(s_list)):
        if  s_list[i-1] > s_list[i]:
            subseq_start = i
        yield s_list[subseq_start:i+1]
    return
def longest_common_list(s_list):
    fwdset = set([tuple(x) for x in sublist(s_list)])
    bwdset = set([tuple(x) for x in sublist(s_list[::-1])])
    commonset = fwdset.intersection(bwdset)
    return list(max(commonset, key=len))
if __name__ == "__main__":
    assert longest_common_list(
        [1, 1, 2, 3, 0, 0, 3, 4, 5, 7, 1, 3, 2, 1, 1, 2]) == [1, 1, 2, 3]