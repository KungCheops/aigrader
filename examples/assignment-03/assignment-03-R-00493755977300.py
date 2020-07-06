def sublist(s_list):
    for i in range(len(s_list) - 1):
        tmp = i
        while i < len(s_list) - 1 and s_list[i + 1] >= s_list[i]:
            yield s_list[tmp:i + 1]
            i += 1
        yield s_list[tmp:i + 1]
    return
def longest_common_list(s_list):
    list_normal = [_ for _ in sublist(s_list)]
    list_reversed = [_ for _ in sublist(s_list[::-1])]
    common_elements = [_ for _ in list_normal if _ in list_reversed]
    return max(common_elements, key=len)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]