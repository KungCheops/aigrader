def sublist(s_list):
    a = s_list[0]
    asc = []
    for s in s_list:
        if s >= a:
            asc.append(s)
            a = s
        if s < a:
            yield asc 
            asc = []
            asc.append(s)
            a = s
    yield asc 
def longest_common_list(s_list):
    common = [s for s in sublist(s_list) for r in sublist(list(reversed(s_list))) if s == r] 
    common.sort(key=len, reverse=True) 
    return common[0]
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]