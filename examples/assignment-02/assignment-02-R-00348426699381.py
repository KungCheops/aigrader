def encode_list(s_list):
    curr=s_list[0]
    count=0
    for char in s_list:
        if char==curr:
            count+=1
        else:
            yield [curr,count]
            curr=char
            count=1
    yield[curr,count]
def create_list (s_list):
    encoded_list=[]
    enc=encode_list(s_list)
    for e in enc:
        encoded_list.append(e)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1,1,1,2,3,3,4,4,5,1,1,7,5]) == [[1, 3],[2, 1],[3, 2],[4, 2],[5, 1],[1, 2],[7, 1],[5, 1]]
    assert create_list(['w','w','w','w','a','a','a','d','e','x','x','x','x','x','x']) == [['w', 4],['a', 3],['d', 1],['e', 1],['x', 6]]