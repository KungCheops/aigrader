def sublist(s_list):
    asc = []
    for i in range(len(s_list)-1):
        if s_list[i] <= s_list[i+1]:
            asc.append(s_list[i])
            if i + 1 == len(s_list)-1:
                asc.append(s_list[i+1])
                yield asc
        else:
            asc.append(s_list[i])
            yield asc
            asc = []
def longest_common_list(s_list):
    return max([x for x in sublist(s_list) for y in sublist(s_list[::-1]) if x == y], key=len)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]