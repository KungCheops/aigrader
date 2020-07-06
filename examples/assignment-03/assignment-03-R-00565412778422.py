def sublist(s_list):
    a = s_list[0]
    b = []
    for x in s_list:
        if x >= a:
            b.append(x)
            a = x
        if x < a:
            yield b 
            b = []
            b.append(x)
            a = x
    yield b 
def longest_common_list(s_list):
    list_c = sublist(s_list) 
    reversed_s_list = list(reversed(s_list))
    list_d = sublist(reversed_s_list) 
    common_sublists = [c for c in list_c for d in list_d if c == d] 
    common_sublists.sort(key=len, reverse=True) 
    longestCommonSublist = common_sublists[0] 
    return longestCommonSublist
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]