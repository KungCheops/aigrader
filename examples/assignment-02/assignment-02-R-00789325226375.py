def encode_list(s_list):
    prev = s_list[0]
    n = 0
    for v in s_list[1:]:
        n+=1
        if v != prev:
            yield [prev, n]
            n=0
        prev = v
    yield [prev, n+1]
def create_list (s_list):
    return list(encode_list(s_list))
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]