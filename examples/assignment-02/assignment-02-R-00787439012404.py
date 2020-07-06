def rle(s_list):
    count = 1 
    for i in range(len(s_list)): 
        temp=s_list[i] 
        if i==len(s_list)-1: 
            yield [temp, count]
        else: 
            if temp==s_list[i+1]: 
                count+=1
            else: 
                yield [temp, count]
                count=1
def encode_list(s_list):
    return rle(s_list)
def create_list (s_list):
    encoded_list=[]
    for x in encode_list(s_list):
        encoded_list.append(x)
    return encoded_list
if __name__ == "__main__":
    print(create_list([1, 1, 1, 2, 2, 2, 1, 1]))
    print(create_list(['a', 'b', 'b', 'c']))
    print(create_list([1, 1, 1]))
    print(create_list([]))
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]