def sublist(s_list):
    sub = []
    s_prev = 0
    for s in s_list:
        if s >= s_prev:
            sub.append(s)
        else:
            yield sub
            sub = [s]
        s_prev = s
    return
def longest_common_list(s_list):
    list_1 = list(sublist(s_list))
    s_list.reverse()
    list_2 = list(sublist(s_list))
    matching = [sub for sub in list_1
                if any(sub == sub_2 for sub_2 in list_2)]
    return max(matching, key=len)
if __name__ == "__main__":
    assert longest_common_list([1, 1, 2, 3, 0, 0, 3, 4, 5, 7, 1, 3, 2, 1, 1, 2]) == [1, 1, 2, 3]