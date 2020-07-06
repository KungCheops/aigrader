def sublist(s_list):
    sublist = []
    for i in range(len(s_list)):
        if i == len(s_list) - 1:
            sublist.append(s_list[i])
            yield sublist.copy()
            break
        p = i
        while True:
            sublist.append(s_list[p])
            yield sublist.copy()
            p += 1
            if p >= len(s_list) or s_list[p] < s_list[p - 1]:
                break
        sublist = []
    return
def longest_common_list(s_list):
    common_list = [i for i in sublist(s_list) if i in sublist(s_list[::-1])]
    return max(common_list, key=len)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]