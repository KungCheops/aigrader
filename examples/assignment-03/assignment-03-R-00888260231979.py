def sublist(s_list):
    for i in range(len(s_list)):
        yield [s_list[i]]
        for j in range(i+1, len(s_list)):
            if s_list[j] >= s_list[j-1]:
                yield s_list[i:j+1]
            else:
                break
def longest_common_list(s_list):
    s_list_reversed = [x for x in reversed(s_list)]
    matching_sublists = [l1 for l1 in sublist(s_list_reversed)
                        for l2 in sublist(s_list) if l1 == l2]
    return max(matching_sublists, key=len)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]