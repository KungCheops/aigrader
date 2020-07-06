def sublist(s_list):
    i = 0
    while (i <= len(s_list) - 1) :
        temp_list = []
        temp_list.append(s_list[i])
        j = i + 1
        while (j <= len(s_list) - 1) :
            if s_list[i] == s_list[j] or s_list[i] == s_list[j] - 1:
                temp_list.append(s_list[j])
                j = j + 1
                i = i + 1
            else:
                break
        yield temp_list
        i = j
    return
def longest_common_list(s_list):
    largest_common_sublist =  [x for x in sublist(s_list) if x in sublist(s_list[::-1])]
    return max(largest_common_sublist, key=len)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]