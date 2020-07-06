def sublist(s_list):
    sublist = []
    for x in s_list:
        if len(sublist):
            if sublist[-1] <= x:
                sublist.append(x)
            elif len(sublist) > 1:
                yield sublist
                sublist=[x]
            else:
                sublist=[x]
        else:
            sublist.append(x)
    yield sublist
def longest_common_list(s_list):
    reversed_list=s_list[::-1]
    sublist1 = []
    sublist2 = []
    for x in sublist(s_list):
        sublist2.append(x)
    for i in sublist(reversed_list):
        sublist1.append(i)
    common_list = [elem for elem in sublist1 if elem in sublist2]
    longest_common_list = max(common_list, key=len)
    return longest_common_list
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1, 1, 2, 3]