def encode_list(s_list):
    prev = s_list[0]
    c = 0
    for s in s_list:
        if s == prev:
            c += 1
        else:
            yield [prev, c]
            c = 1
        prev = s
    yield [prev, c]
def create_list (s_list):
    encoded_list=[]
    gen = encode_list(s_list)
    count = next(gen)
    while count is not None:
        encoded_list.append(count)
        try:
            count = next(gen)
        except StopIteration:
            return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]