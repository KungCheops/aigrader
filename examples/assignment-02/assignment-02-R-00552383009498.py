def encode_list(s_list):
    c = s_list[0]
    n = 0
    for e in s_list:
        if e != c:
            yield [c, n]
            n = 0
            c = e
        n += 1
    yield [c, n]
def create_list (s_list):
    encoded_list=list(encode_list(s_list))
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]