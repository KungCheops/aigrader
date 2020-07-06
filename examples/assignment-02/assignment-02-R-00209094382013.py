def encode_list(s_list):
    if len(s_list) == 0:
        return
    prev = s_list[0]
    n = 0
    for x in s_list:
        if x == prev:
            n += 1
        else:
            yield [prev, n]
            prev = x
            n = 1
    yield [prev, n]
def create_list(s_list):
    return list(encode_list(s_list))
if __name__ == "__main__":
    list_in = [1, 1, 1, 2, 3, 3, 4, 4, 5, 1, 1, 7, 5]
    list_out = [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]
    list_result = create_list(list_in)
    assert list_result == list_out