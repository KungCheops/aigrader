def sublist(s_list):
    for i in range(len(s_list)): 
        e = s_list[i]
        for j in range(i + 1, len(s_list)): 
            seq = s_list[j]
            if (seq >= e):
                yield s_list[i:j+1]
                e = seq
            else:
                break
def longest_common_list(s_list):
    l = [i for i in sublist(s_list)]
    inv = [j for j in sublist([i for i in s_list[::-1]])]
    common = [c for c in l if c in inv]
    longest_sublist = [m for m in max(common, key=len)]
    return longest_sublist
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]