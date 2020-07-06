def sublist(s_list):
    current_list = [s_list[0]]
    for current in s_list[1:]:
        if current < current_list[-1]:
            yield current_list
            current_list = [current]
        else:
            current_list.append(current)
    yield current_list
def longest_common_list(s_list):
    sublists = sublist(s_list)
    sublists_reversed = sublist(s_list[::-1])
    sublists_reversed_list = [a for a in sublists_reversed]
    common_lists = filter(lambda l: l in sublists_reversed_list, sublists)
    return max(common_lists, key=len)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1, 1, 2, 3]