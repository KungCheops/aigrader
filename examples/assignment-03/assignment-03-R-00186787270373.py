from itertools import product
def sublist(s_list):
    i = 0
    j = 0
    N = len(s_list)
    while j < N:
        while j < N-1 and s_list[j] <= s_list[j+1]:
            j += 1
        j += 1
        yield s_list[i:j]
        i = j
    return
def longest_common_list(s_list):
    lists = sublist(s_list)
    lists_reversed = sublist(list(reversed(s_list)))
    lists_common = [l1 for l1, l2 in product(lists, lists_reversed) if l1==l2]
    return max(lists_common, key=len)
if __name__ == "__main__":
    test_list = [1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]
    assert longest_common_list(test_list) == [1,1,2,3]