def encode_list(s_list):
    if len(s_list) < 1:
        return
    active, count = s_list[0], 1
    for elem in s_list[1:]:
        if elem == active:
            count += 1
        else:
            yield [active, count]
            active, count = elem, 1
    yield [active, count]
def create_list(s_list):
    encoded_list = [x for x in encode_list(s_list)]
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1, 1, 7, 5]) == [
        [1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]
    assert create_list([1, 1, 1]) == [[1, 3]]
    assert create_list([]) == []
    assert create_list([1]) == [[1, 1]]
    assert create_list("CAAAAAAGGGT") == [
        ['C', 1], ['A', 6], ['G', 3], ['T', 1]]