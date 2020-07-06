def sublist(s_list):
    last = None
    cur = []
    for val in s_list:
        if last == None or val >= last:
            cur.append(val)
            last = val
        else:
            yield cur
            cur = [val]
            last = val
def longest_common_list(s_list):
    orig_order = [s for s in sublist(s_list)]
    s_list.reverse()
    rev_order = [s for s in sublist(s_list)]
    count = -1
    for l in orig_order:
        l_count = len(l)
        if l_count > count:
            for l_rev in rev_order:
                if l == l_rev:
                    count = l_count
                    ret = l_rev
                    break
    return ret
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]