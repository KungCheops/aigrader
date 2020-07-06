def sublist(s_list):
    it = iter(s_list) 
    prev, res = next(it), [] 
    while prev is not None: 
        start = next(it, None) 
        if prev <= start:
            res.append(prev)              
        else:
            yield list(res + [prev]) 
            res = [] 
        prev = start
def longest_common_list(s_list):
    r_list=list(s_list)
    r_list.reverse()
    l1 = list(sublist(s_list))
    l2 = list(sublist(r_list))
    lst = [i for i in l1 if i in l2]
    maxList = max(lst, key = len)
    return maxList
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]