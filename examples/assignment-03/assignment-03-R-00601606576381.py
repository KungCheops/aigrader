def sublist(s_list):
    start_index = 0
    end_index = 0
    sub = []
    for x, y in zip(s_list, s_list[1:]): 
        end_index += 1
        if y < x: 
            for i in range(start_index, end_index):
                sub.append(s_list[i])
            yield sub
            sub = [] 
            start_index = end_index
    return
def longest_common_list(s_list):
    r_list = list(reversed(s_list))             
    sublists_original = list(sublist(s_list))   
    sublists_reverse  = list(sublist(r_list))   
    common_sublists = [e for e in sublists_original if e in sublists_reverse] 
    common_sublists.sort(key=len, reverse=True)
    return common_sublists[0] 
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]