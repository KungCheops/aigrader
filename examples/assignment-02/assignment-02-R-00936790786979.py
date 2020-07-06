def encode_list(s_list):
    run_length = 1
    for i, (x, y) in enumerate(zip(s_list, s_list[1:])): 
        if x == y:
            run_length += 1
        else:
            yield [x, run_length] 
            run_length = 1
        if (i == len(s_list) - 2): 
            yield [y, run_length]
    return
def create_list (s_list):
    encoded_list=[]
    for pair in encode_list(s_list):
        encoded_list.append(pair)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]