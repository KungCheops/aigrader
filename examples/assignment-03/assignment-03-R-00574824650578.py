def sublist(s_list):
    for i in range(0, len(s_list)):
        for j in range(i+1, len(s_list)):
            if s_list[j] >= s_list[j-1]:
                yield s_list[i:j+1]
            else:
                break
def longest_common_list(s_list):
    sublists = [sublist for sublist in sublist(s_list)]
    s_list.reverse()
    sublistsReversed = [reversedSublist for reversedSublist in sublist(s_list)]
    common = [list1 for list1 in sublists for list2 in sublistsReversed if list1 == list2]
    longestCommonSublist, length = [],0
    for subList in common:  
        if  length < len(subList):
            length = len(subList)
            longestCommonSublist = subList
    return longestCommonSublist
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]