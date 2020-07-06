def encode_list(s_list):
    element=s_list[0]
    count=0
    for  i in s_list:
        if i==element: count+=1
        else:
            yield [element,count]
            element=i
            count=1
    yield[element,count]
def create_list (s_list):
    encoded_list=list(encode_list(s_list))
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]
    assert create_list([11, 11, 22, 22, 22, 22, 33, 44, 44, 44,44,44,55]) == [[11,2], [22, 4], [33, 1], [44, 5], [55, 1]]
    assert create_list(['C','C','A','B','B','B','B']) == [['C',2], ['A', 1], ['B', 4]]