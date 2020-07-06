def encode_list(s_list):
    datavalue_x = s_list[0]
    count = 0
    for datavalue_y in s_list:
        if datavalue_y == datavalue_x:
            count += 1
        else:
            yield [datavalue_x, count]
            datavalue_x = datavalue_y
            count = 1
    yield [datavalue_x, count]
    return
def create_list(s_list):
    encoded_list=[]
    encoded_datavalue = encode_list(s_list)
    for datavalues in encoded_datavalue:
            encoded_list.append(datavalues)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]