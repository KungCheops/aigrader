def encode_list(s_list):
    character=s_list[0]   
    count=0               
    for instance in s_list:          
        if instance == character:      
            count=count+1      
        else:          
            yield [character,count]    
            count=1                    
            character=instance
    yield  [character,count]          
    return
def create_list (s_list):
    encoded_list=[]
    encoded_list=list(encode_list(s_list))
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]