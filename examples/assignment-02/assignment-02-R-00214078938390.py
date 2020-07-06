def encode_list(s_list):
    pre_i=s_list[0]
    count=1
    for i in s_list[1:]:
        if i!=pre_i:
            yield [pre_i,count]
            pre_i=i
            count=1
        else:
            count+=1    
    yield [pre_i,count] 
    return
def create_list (s_list):
    encoded_list=[]
    for i in encode_list(s_list):
        encoded_list.append(i) 
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]
    assert create_list(['H','A','L','L','O']) == [['H', 1], ['A', 1], ['L', 2], ['O', 1]]