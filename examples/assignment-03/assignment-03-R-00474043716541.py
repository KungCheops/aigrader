def sublist(s_list):
    data_values = [s_list[0]]
    for element in s_list[1:]:
        if data_values[-1] > element:
            yield data_values
            data_values = [element]
        else:
            data_values.append(element)
    yield data_values
    return
def longest_common_list(s_list):
    sub_lists = list(sublist(s_list))
    sub_lists_reversed = list(sublist(s_list[::-1]))
    longest_common_sublist = [element for element in sub_lists for element1 in sub_lists_reversed if
                              element == element1]
    longest_common_sublist = max(longest_common_sublist, key=len)
    return longest_common_sublist
if __name__ == "__main__":
    assert longest_common_list([1, 1, 2, 3, 0, 0, 3, 4, 5, 7, 1, 3, 2, 1, 1, 2]) == [1, 1, 2, 3]