def sublist(s_list):
    start_elem=s_list[0]                                   
    list_asc=[]                                            
    for elem in s_list:                                    
        if elem >= start_elem:       
            list_asc.append(elem)
            start_elem=elem                                
        else:                           
            yield list_asc                                 
            list_asc=[elem]                                
            start_elem=elem                                
def longest_common_list(s_list):
    original_list=sublist(s_list)
    rev_list=sublist(s_list[::-1])   
    common_list=[i for i in original_list if i in rev_list] 
    common_list.sort(key=len,reverse=True)                  
    return common_list[0]                                   
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]