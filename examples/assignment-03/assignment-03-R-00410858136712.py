def sublist(s_list):
    yield []
    x = 0
    for i in range(len(s_list)):
        if s_list[i] < s_list[i-1]:
            x = i
        yield s_list[x:i+1]
    return
def longest_common_list(s_list):
    forward = set([tuple(x) for x in sublist(s_list)])
    backward = set([tuple(x) for x in sublist(s_list[::-1])])
    both = forward.intersection(backward)
    return list(max(both, key=len))
if __name__ == "__main__":
    assert longest_common_list(
        [1, 1, 2, 3, 0, 0, 3, 4, 5, 7, 1, 3, 2, 1, 1, 2]) == [1, 1, 2, 3]