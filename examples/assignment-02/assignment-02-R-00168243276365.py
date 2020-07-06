def encode_list(s_list):
    curr = s_list[0]
    count = 1
    for nxt in s_list[1:]:
        if curr == nxt:
            count += 1
        else:
            yield (curr, count)
            curr = nxt
            count = 1
    yield (curr, count)
def create_list (s_list):
    return [[val, count] for val, count in encode_list(s_list)]
if __name__ == "__main__":
    l = [1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]
    assert create_list(l) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]