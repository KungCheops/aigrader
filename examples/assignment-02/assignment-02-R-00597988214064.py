def encode_list(s_list):
    val = s_list[0]
    ret = [val, 0]
    for i in range(len(s_list)):
        if s_list[i] == val :
            ret[1] += 1
        else:
            yield ret
            val = s_list[i]
            ret = [val, 1]
    yield ret
    return
def create_list (s_list):
    encoded_list=[]
    i = encode_list(s_list)
    for val in i:
        encoded_list.append(val);
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]