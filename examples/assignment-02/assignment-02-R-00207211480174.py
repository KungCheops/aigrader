def encode_list(s_list):
    s_list.append('')
    aTuple = [s_list[0], 0]
    for n in s_list:
        if n == aTuple[0]:
            aTuple[1] += 1
        else:
            yield [aTuple[0], aTuple[1]] 
            aTuple[0] = n
            aTuple[1] = 1
def create_list (s_list):
    encoded_list=[]
    encoded_list = [aTuple for aTuple in encode_list(s_list)]
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]
    assert create_list([1,1,1,1,1,1, 2,2,2,2, 3, 4,4,4,4,4,4,4,4,4,4, 5, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, 7, 5]) == [[1, 6], [2, 4], [3, 1], [4, 10], [5, 1], [1, 15], [7, 1], [5, 1]]
    assert create_list(['1', '1', '1', '2', '3', '3', '4', '4', '5', '1','1','7','5']) == [['1', 3], ['2', 1], ['3', 2], ['4', 2], ['5', 1], ['1', 2], ['7', 1], ['5', 1]]
    assert create_list(['a', 'a', 'a', 'b', 'c', 'c', 'd', 'd', 'e', 'a', 'a', 'g', 'e']) == [['a', 3], ['b', 1], ['c', 2], ['d', 2], ['e', 1], ['a', 2], ['g', 1], ['e', 1]]
    assert create_list([]) == []