def sublist(s_list):
    first_element=0
    last_element=1
    while last_element<len(s_list):
        if s_list[last_element]>=s_list[last_element-1]:
            yield s_list[first_element:last_element+1]
            last_element=last_element+1
        else:
             first_element=last_element
             last_element=last_element+1
def longest_common_list(s_list):
    sublists=list(sublist(s_list))
    reversed_sublists=list(sublist(list(reversed(s_list))))
    longest_common=max([element for element in sublists if element in reversed_sublists], key=len)
    return longest_common
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]
    assert longest_common_list([1,2,3,2,2,1,3,2,1])==[1,2,3]
    assert longest_common_list([1,2,3,4,5,0,0,1,2,1])==[1,2]
    assert longest_common_list([1,2,1,0,3,4,5,0,1,2,1])==[0, 1, 2]