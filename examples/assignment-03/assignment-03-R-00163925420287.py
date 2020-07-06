def sublist(s_list):
    temp_list = []
    for elem in s_list:
        if len(temp_list) == 0 or temp_list[-1] <= elem:
            temp_list.append(elem)
        else:
            yield temp_list
            temp_list = [elem]
    yield temp_list
def longest_common_list(s_list):
    sublist_forward = [l for l in sublist(s_list)]
    common_sublists = [l for l in sublist(s_list[::-1]) if l in sublist_forward]
    return max(common_sublists, key=len)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1, 1, 2, 3]
    assert longest_common_list([1,2,3,2,2,1,3,2,1]) == [1, 2, 3]
    assert longest_common_list([1,2,1]) == [1,2]
    assert longest_common_list([1]) == [1]
    assert longest_common_list([]) == []