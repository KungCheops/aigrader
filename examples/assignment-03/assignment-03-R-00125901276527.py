def sublist(s_list):
    i = 0
    while i < len(s_list):
        l = []
        l.append(s_list[i])
        j = 0
        while i + j + 1 < len(s_list) and s_list[i + j + 1] >= s_list[i + j]:
            l.append(s_list[i + j + 1])
            j += 1
        yield l
        i += j + 1
    return
def longest_common_list(s_list):
    l = []
    r = [i for i in sublist([i for i in reversed(s_list)])]
    for i in [i for i in sublist(s_list)]:
        if (i in r and len(i) > len(l)):
            l = i
    return l
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]