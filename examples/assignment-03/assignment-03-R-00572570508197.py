def sublist(s_list):
    for i in range(len(s_list)+1):
        for j in range(i+1, len(s_list)+1):
            if(s_list[i:j] == sorted(s_list[i:j])):
                yield(s_list[i:j])
    return
def longest_common_list(s_list):
    lista1 = list(sublist(s_list))
    lista2 = list(sublist(s_list[::-1]))
    ls1 = [elem for elem in lista1 if elem in lista2]
    return max(ls1, key=len)
if __name__ == "__main__":
    assert longest_common_list(
        [1, 1, 2, 3, 0, 0, 3, 4, 5, 7, 1, 3, 2, 1, 1, 2]) == [1, 1, 2, 3]