def encode_list(s_list):
    count = 0
    data_value = s_list[0]
    for element in s_list:
        if data_value != element:
            yield [data_value, count]
            data_value = element
            count = 1
        else:
            count += 1
    yield [data_value, count]
    return
def create_list(s_list):
    encoded_list = []
    encoded_list = list(encode_list(s_list))
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1, 1, 7, 5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2],
                                                                    [7, 1], [5, 1]]