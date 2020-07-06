def sublist(s_list):
    it = iter(s_list)
    a = next(it) 
    singles = []
    sublist = [a]
    while a is not None:
        singles.append(a)        
        yield singles
        singles = []
        b = next(it, None)            
        if b is not None and b >= a:             
            sublist.append(b)                         
            yield sublist
        else:                                     
            sublist = [b]                                        
        a = b    
    return 
def longest_common_list(s_list):    
    sublists = []
    for i in sublist(s_list):
        sublists.append(list(i))
    sublists_reversed = []
    for i in sublist(s_list[::-1]):
        sublists_reversed.append(i)
    common_sublists = []
    for i in sublists:
        for j in sublists_reversed:
            if i == j:                 
                common_sublists.append(i)
    longest_common_sublist = []
    for item in common_sublists:
        if len(item) > len(longest_common_sublist):
            longest_common_sublist = item
    return longest_common_sublist
if __name__ == "__main__":
    assert longest_common_list([1,2,3,1]) == [1]
    assert longest_common_list([1,2,3,2,2,1,3,2,1]) == [1,2,3]
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1,2,3]