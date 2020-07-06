def sublist(s_list):
    sublist = []
    last = None
    for i in range(len(s_list)):
        current = s_list[i]
        if last != None and last > current:
            sublist = []
        sublist.append(current)
        yield sublist.copy()
        last = current
    yield sublist
    return
def longest_common_list(s_list):
    reverse_list = [elem for elem in reversed(s_list)]
    common_list = [elem for elem in sublist(s_list) if elem in sublist(reverse_list)]
    longest_list = max(common_list, key=len)
    return longest_list
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]