def reversed(l):
    return l[::-1]
def sublist(s_list):
    i = 0
    while i < len(s_list):
        i += 1
        l = [s_list[i-1]]
        while i < len(s_list) and (s_list[i] >= s_list[i-1]):
            l.append(s_list[i])
            i += 1
        yield l
def longest_common_list(s_list):
    sublists = [l for l in sublist(s_list)]
    sublists_rev = [l for l in sublist(reversed(s_list))]
    common_sl_len = 0
    common_sl = None
    for sl in sublists:
        for sl_rev in sublists_rev:
             if sl == sl_rev and len(sl_rev) > common_sl_len:
                common_sl = sl_rev
                common_sl_len = len(common_sl)
    """
    i = 0
    for sl in sublists:
        j = i
        while j < len(sublists_rev):
            sl_rev = sublists_rev[j]
            if sl == sl_rev and len(sl_rev) > common_sl_len:
                common_sl = sl_rev
                common_sl_len = len(common_sl)
            j += 1
        i += 1
    """
    return common_sl
if __name__ == "__main__":
    l1 = [1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]
    l2 = [1,2,3,2,2,1,3,2,1]
    assert longest_common_list(l2) == [1, 2, 3]