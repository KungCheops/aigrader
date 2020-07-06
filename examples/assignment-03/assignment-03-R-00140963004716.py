def sublist(s_list):
    tmp = []
    reference = s_list[0]
    for i in range(1, len(s_list)):
        tmp.append(reference)
        if s_list[i] >= reference:
            reference = s_list[i]
        else:
            yield tmp
            tmp = []
            reference = s_list[i]
    tmp.append(reference)
    yield tmp
def longest_common_list(s_list):
    org, rev = sublist(s_list), sublist(s_list[::-1])
    longest_sublist = max([a for a in org for b in rev if a == b], key=len)
    return longest_sublist
if __name__ == "__main__":
    assert longest_common_list([1, 1, 2, 3, 0, 0, 3, 4, 5, 7, 1, 3, 2, 1, 1, 2]) == [1, 1, 2, 3]