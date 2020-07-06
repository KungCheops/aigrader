def sublist(s_list):
    sub_list1 = []
    for i in range(len(s_list)-1):
        sub_list1.append(s_list[i])
        if s_list[i] > s_list[i+1]:
            yield list(sub_list1)
            sub_list1 = []
def longest_common_list(s_list):
    main_list = sublist(s_list)
    reversed_list = sublist([element for element in reversed(s_list)])
    common_elements = [element for element in main_list if element in reversed_list]
    common_elements.sort(key = len, reverse = True)
    return common_elements[0]
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]