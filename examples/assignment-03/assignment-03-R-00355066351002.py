def sublist(s_list):
    s_list_len = len(s_list)
    for i in range(s_list_len):
        sub_list_len = 0
        for j in range(i, s_list_len - 1):
            if s_list[j] + 1 == s_list[j+1] or s_list[j] == s_list[j+1]:
                sub_list_len += 1
            else:
                break
        if sub_list_len > 0:
            yield s_list[i:i + sub_list_len+1]
    return
def longest_common_list(s_list):
    ord_list_sub_lists = [i for i in sublist(s_list)]
    ord_list_sub_lists.sort(key=len, reverse=True)
    rev_s_list = [s_list[i] for i in range(len(s_list)-1, -1, -1)]
    rev_list_sub_lists = [i for i in sublist(rev_s_list)]
    rev_list_sub_lists.sort(key=len, reverse=True)
    common_sublists = [] 
    longest_sublist = None
    if len(ord_list_sub_lists) < len(rev_list_sub_lists):
        common_sublists = [sublist_i for sublist_i in ord_list_sub_lists if sublist_i in rev_list_sub_lists]
    else:
        common_sublists = [sublist_i for sublist_i in rev_list_sub_lists if sublist_i in ord_list_sub_lists]
    if len(common_sublists) > 0:
        longest_sublist = common_sublists[0]
    return longest_sublist
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]