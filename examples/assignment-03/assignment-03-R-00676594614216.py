def sublist(s_list):
    if s_list == []:
        return []
    s_list_iter = iter(s_list)
    prev_value = next(s_list_iter)
    curr_list  = [prev_value]
    for item in s_list_iter:
        if item < prev_value:
            yield curr_list
            curr_list = [item]
        else:
            curr_list.append(item)
        prev_value = item
    yield curr_list
    return
def longest_common_list(s_list):
    sublist_generator           = sublist(s_list)
    sublist_generator_reversed  = sublist(reversed(s_list))
    return max([s for s in sublist_generator if s in sublist_generator_reversed], key=len)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]