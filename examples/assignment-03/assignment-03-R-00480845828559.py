def sublist(s_list):
    if len(s_list) == 0:
        yield []
    else:
        t = s_list[0]
        l = [s_list[0]]
        for i in range(1,len(s_list)):
            if s_list[i] == t or s_list[i] == (t+1):
                l += [s_list[i]]
                t = s_list[i]
            else:
                yield l
                t = s_list[i]
                l = [s_list[i]]
        yield l
def longest_common_list(s_list):
    g_l1 = [(len(e), e) for e in sublist(s_list)]
    s_list.reverse()
    g_l2 = [(len(e), e) for e in sublist(s_list)]
    l = g_l1 + g_l2
    l.sort(key = lambda x: x[0], reverse=True)
    return l[0][1]
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]