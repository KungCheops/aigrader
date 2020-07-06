import numpy as np
def sublist(s_list):
    for i in range(len(s_list)):
        for j in (range(i,len(s_list))):
            if is_asc(s_list[i:j+1]) and s_list[i:j+1] != s_list:
                yield s_list[i:j+1]
def is_asc(s_list):
    i = 0
    while i < len(s_list)-1:
        if s_list[i] > s_list[i+1]:
            return False
        i += 1
    return True
def longest_common_list(s_list):
    gen = sublist(s_list)
    res = [g for g in gen for i in range(len(s_list)-len(g)+1) if (g[::-1] == s_list[i:i+len(g)])]
    return max(res, key = len)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1,2,3]