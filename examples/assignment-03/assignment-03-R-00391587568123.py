def returnAscending(s_list):
    counter=0
    for i in range(1, len(s_list)):
        if i==len(s_list)-1:
            if s_list[i]>=s_list[i-1]:
                counter+=1
                yield s_list[i-counter:i+1]
            else:
                if counter>0:
                    yield s_list[i-counter-1:i]
        else:
            if s_list[i]>=s_list[i-1]:
                counter+=1
            else:
                if counter > 0:
                    yield s_list[i-counter-1:i]
                counter=0
def sublist(s_list):
    asc_lists=[]
    for x in returnAscending(s_list):
        asc_lists.append(x)
    return asc_lists
def longest_common_list(s_list):
    r_list=[]
    [r_list.append(x) for x in reversed(s_list)]
    acs_lists=sublist(s_list)
    acs_lists_r=sublist(r_list)
    common_lists=[]
    [common_lists.append(x) for x in acs_lists if x in acs_lists_r]
    if len(common_lists)>0:
        length=[]
        [length.append(len(x)) for x in common_lists]
        maxval=max(length)
        indices=[]
        [indices.append(i) for i in range(len(length)) if length[i]==maxval]
        LCL=[]
        [LCL.append(common_lists[i]) for i in indices]
        if len(LCL)==1:
            return LCL[0]
        else:
            return LCL
    else:
        return common_lists
if __name__ == "__main__":
    print(sublist([5, 1, 2, 3, 4, 1, 2, 1, 1, 5, 6, 2, 2, 3, 0]))
    print(longest_common_list([5, 1, 2, 3,4, 4, 3, 2, 1, 8, 7, 6,1, 1, 6, 7, 8]))
    print(longest_common_list([5, 1, 2, 3, 3, 2, 1, 8]))
    print(longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]))
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]