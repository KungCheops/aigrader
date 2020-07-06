def encode_list(s_list):
    token = s_list[0]
    count = 0
    for e in s_list:
        if e == token:
            count += 1
        else:
            yield [token, count]
            token = e
            count = 1
    yield [token, count]
def create_list (s_list):
    return list(encode_list(s_list))
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]