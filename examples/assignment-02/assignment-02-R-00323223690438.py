def encode_list(s_list):
    count = 0
    token = s_list[0]
    for s in s_list:
        if (s == token):
            count += 1
        else:
            yield [token, count]
            token = s
            count = 1
    yield [token, count]
def create_list (s_list):
    encoded_list=[s for s in encode_list(s_list)]
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]