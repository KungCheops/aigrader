import numpy as np
def sublist(s_list):
    count = 1
    prev = []
    x = []
    for char in s_list:
        if char != prev:
            if prev:
                entry = prev
                x.append(entry)
            count = 1
            prev = char
        else:
            count += 1
    return x
def longest_common_list(s_list) :
    s_list = sublist(s_list)
    s_list.reverse()
    m = 1
    li = 1
    max = 0
    for i in range(0, len(s_list)) :
        if (s_list[i] > s_list[i-1]) :
            li =li + 1
        else :
            if (m <= li)  :
                m = li
                max = i - m
            li = 1
    if (m < li) :
        m = li
        max = len(s_list) - m
    x = []
    for i in range(max, (m+max)) :
        x.append(s_list[i])
    x.insert(0,li)
    return( x)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1,2,3]