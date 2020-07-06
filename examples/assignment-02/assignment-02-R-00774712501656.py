def encode_list(s_list):
    sub_list = s_list
    while len(sub_list) > 0:
        data_value = sub_list[0]
        for i, e in enumerate(sub_list + [0]):
            if e == data_value and i != len(sub_list):
                continue
            else:
                del sub_list[:i]
                yield [data_value, i]
                break
def create_list (s_list):
    gen = encode_list(s_list)
    return list(gen)
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]