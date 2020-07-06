def sublist(s_list):
    if not s_list:
        return
    sub = []
    for s in s_list:
        if sub and sub[-1] > s:
            yield sub
            sub = [s]
        else:
            sub.append(s)
    yield sublist
def longest_common_list(s_list):
    sublists_regular = [sub for sub in sublist(s_list)]
    s_list.reverse()
    sublists_common = [sub for sub in sublist(s_list) if sub in sublists_regular]
    longest_common = max(sublists_common, key=lambda sub: len(sub))
    return longest_common
if __name__ == "__main__":
    assert longest_common_list([1, 1, 2, 3, 0, 0, 3, 4, 5, 7, 1, 3, 2, 1, 1, 2]) == [1, 1, 2, 3]