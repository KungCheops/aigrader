def sublist(s_list):
    b = []
    for i in range(len(s_list)):
        temp = []
        temp.append(s_list[i])
        if temp not in b:
            b.append(temp)
            yield temp
        for j in range(i, len(s_list) - 1):
            if s_list[j + 1] >= s_list[j]:
                temp = temp + [s_list[j + 1]]
                if temp not in b:
                    b.append(temp)
                    yield temp
            else:
                temp = []
                temp.append(s_list[j + 1])
                if temp not in b:
                    b.append(temp)
                    yield temp
    return
def longest_common_list(s_list):
    l = [x for x in sublist(s_list)]
    s_list.reverse()
    l_reverse = [x for x in sublist(s_list) if x in l]
    return max(l_reverse, key=lambda i: len(i))
if __name__ == "__main__":
    assert longest_common_list([1, 1, 2, 3, 0, 0, 3, 4, 5, 7, 1, 3, 2, 1, 1, 2]) == [1, 1, 2, 3]