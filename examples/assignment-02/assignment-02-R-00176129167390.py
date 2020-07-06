def encode_list(s_list):
    counter = 1
    for i in range(len(s_list)):
        if(i == len(s_list)-1):
            yield [s_list[i], counter]
        elif (s_list[i] != s_list[i+1]):
            yield[s_list[i], counter]
            counter = 1
        else:
            counter += 1
    return
def create_list (s_list):
    return list(encode_list(s_list))
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]
    assert create_list("aaabccadee") == [['a', 3],['b', 1],['c', 2],['a', 1],['d', 1], ['e', 2]]    
    assert create_list('a') == [['a', 1]]