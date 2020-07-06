def encode_list(s_list):
    i = 0
    while i < len(s_list):                
        multiples_index = i + 1
        while multiples_index < len(s_list):            
            if s_list[i] != s_list[multiples_index]:    
                break;
            multiples_index += 1
        yield [s_list[i], multiples_index-i]            
        i = multiples_index   
    return
def create_list (s_list):
    encoded_list=[]
    return list(encode_list(s_list))
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]