def encode_list(s_list):
    prev = None
    count = 0
    for elem in s_list:
        if prev == None:
            prev = elem
            count = count + 1
        elif elem == prev:
            count = count + 1
        else:
            result = [prev, count]
            prev = elem
            count = 1
            yield result
    yield [prev, count]
    return
def create_list (s_list):
    encoded_list = [ x for x in encode_list(s_list)]
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]