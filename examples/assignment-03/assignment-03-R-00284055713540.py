def sublist(s_list):
    N = len(s_list)
    prev_sublist = [ s_list[0] ]            
    for i in range(1, N):
        if s_list[i] >= s_list[i-1]:        
            prev_sublist.append(s_list[i])
        else:                               
            yield prev_sublist 
            prev_sublist = [ s_list[i] ]
    yield prev_sublist                      
def longest_common_list(s_list):
    s  = sublist(s_list)
    sr = sublist(list(reversed(s_list)))
    common = [x for x in s for y in sr if x == y] 
    return max(common, key=len, default=[])
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1,2,3]