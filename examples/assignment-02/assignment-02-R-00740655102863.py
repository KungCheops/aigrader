def encode_list(s_list):
    list_obj = [s_list[0], 1]
    for i in s_list[1:]:
        if i != list_obj[0]:
            yield list_obj
            list_obj = [i, 0]
        list_obj[1] += 1
    yield list_obj
def create_list (s_list):
    encoded_list = [i for i in encode_list(s_list)]
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]