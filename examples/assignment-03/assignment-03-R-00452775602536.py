def sublist(s_list):
    mySublist = []
    numberAtIndex = 0
    for i in s_list:
        if i >= numberAtIndex:
            mySublist.append(i)
            numberAtIndex = i
        else:
            yield mySublist
            numberAtIndex = i
            mySublist = [i]
    return 
def longest_common_list(s_list):
    sublista = sublist(s_list)
    reversedList = sublist(list(reversed(s_list)))
    resultlist = [i for i in sublista if i in reversedList]
    return max(resultlist)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1,2,3]