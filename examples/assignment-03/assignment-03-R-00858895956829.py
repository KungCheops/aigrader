def sublist(s_list):
    counter, list_position = 0, 0
    n = len(s_list)
    while counter < n:
        while counter < n-1 and s_list[counter] <= s_list[counter+1]:
            counter += 1
        counter += 1
        yield s_list[list_position:counter]
        list_position = counter
def longest_common_list(s_list):
    s_list_reversed = s_list.copy()
    s_list_reversed.reverse()
    sublist_pairs = [(x,y) for x in sublist(s_list) for y in sublist(s_list_reversed)]
    equal_pairs = [l1 for l1, l2 in sublist_pairs if l1==l2]
    return max(equal_pairs, key=len)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]