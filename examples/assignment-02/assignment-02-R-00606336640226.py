def encode_list(s_list):
    if len(s_list) == 0:
        return
    prev = s_list[0]
    count = 0
    for n in s_list:
        if n == prev:
            count += 1
        else:
            yield [prev, count]
            prev = n
            count = 1
    yield [prev, count]
def create_list (s_list):
    encoded_list=list(encode_list(s_list))
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]