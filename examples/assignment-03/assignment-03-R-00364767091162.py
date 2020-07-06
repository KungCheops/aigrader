def sublist(s_list):
    longest_list = [s_list[0]]
    for i in range(len(s_list) - 1):
        if s_list[i] <= s_list[i+1]:
            longest_list.append(s_list[i+1])
        else:
            yield longest_list
            longest_list = [s_list[i + 1]]
    yield longest_list 
def longest_common_list(s_list):
    forward_lists = list(sublist(s_list))
    reverse_lists = list(sublist(s_list[::-1])) 
    common_lists = [f for f in forward_lists for r in reverse_lists if f == r]
    return max(common_lists, key=len)
if __name__ == "__main__":
 assert longest_common_list([1, 1, 2, 3, 0, 0, 3, 4, 5, 7, 2, 1, 1, 3, 2, 1, 1, 2]) == [1, 1, 2, 3]
 assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1, 1, 2, 3]