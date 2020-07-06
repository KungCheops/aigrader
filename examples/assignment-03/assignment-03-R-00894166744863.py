def sublist(s_list):
    temp = []
    prev = None
    start = 0
    for index, value in enumerate(s_list):
        if value < prev:
            yield s_list[start:index]
            start = index
        if index == len(s_list)-1:
            yield s_list[start:len(s_list)]
        prev = value
    return
def longest_common_list(s_list):
    longest_list = []
    original_gen = sublist(s_list)
    reverse_gen = sublist([x for x in reversed(s_list)])
    original = list(original_gen)
    rev = list(reverse_gen)
    common_lists = [i for i in original for j in rev if i == j ]
    longest_list = max(common_lists, key=len)
    return longest_list
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3] 