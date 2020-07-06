def sublist(s_list):
    k = 0
    while k <= len(s_list) - 1:
        i = k
        sublist = list()
        sublist.append(s_list[i])
        while i != len(s_list) - 1 and (s_list[i + 1] >= s_list[i]): 
            sublist.append(s_list[i + 1])
            i += 1
        k = i + 1
        yield sublist
def find_commons(a, b):
    return [item for item in a if item in b]
def longest_common_list(s_list):
    a = sorted(sublist(s_list), key=len, reverse=True)
    b = sorted(sublist(s_list[::-1]), key=len, reverse=True)
    return max([find_commons(item, item2) for item in a for item2 in b], key=len)
if __name__ == "__main__":
    assert longest_common_list([1, 1, 2, 3, 0, 0, 3, 4, 5, 7, 1, 3, 2, 1, 1, 2]) == [1, 1, 2, 3]