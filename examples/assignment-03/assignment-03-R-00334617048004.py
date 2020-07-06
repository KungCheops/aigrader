def sublist(s_list):
    sub=[s_list[0]]
    yield sub
    for i in s_list[1:]:
        if i>=sub[-1]:
            sub= sub + [i]
            yield sub
        else:    
            sub=[i]
            yield sub
    return
def longest_common_list(s_list):
    sub_list=[i for i in sublist(s_list)]
    s_list.reverse()
    sub_rev= [i for i in sublist(s_list)]
    common_lists= [i for i in sub_list if i in sub_rev]
    longest_common_list=common_lists[0]
    for i in common_lists[1:]:
        if len(i)>len(longest_common_list):
            longest_common_list=i
    return longest_common_list
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]