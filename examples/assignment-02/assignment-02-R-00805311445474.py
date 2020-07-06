def encode_list(s_list):
    key = s_list[0]
    count = 0
    for element in s_list:
        if key != element:
            yield [key, count]
            count = 1
            key = element
        else:
            count += 1
    yield [key, count]
def create_list (s_list):
    encoded_list = [i for i in encode_list(s_list)]
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1, 1, 7, 5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2],
                                                                    [7, 1], [5, 1]]