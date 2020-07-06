def sublist(s_list):
    for i, val in enumerate(s_list):
        if i == 0:
            subs = [[s_list[i]]]
            yield [s_list[i]]
        elif val >= subs[-1][-1]:
            old_sub = subs[-1].copy()
            old_sub.append(val)
            yield old_sub
            subs.append(old_sub)
        else:
            new_sub = [val]
            yield new_sub
            subs.append(new_sub)
def longest_common_list(s_list):
    s_list_r = s_list[::-1]
    s = [l for l in sublist(s_list)]
    r = [l for l in sublist(s_list_r)]
    longest_common = max([l for l in s if l in r], key=len)
    return longest_common
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]