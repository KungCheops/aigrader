def encode_list(s_list):
    curr, count = None, -1
    for item in s_list:
        if item == curr: count += 1
        elif item != curr:
            if count > 0: yield [curr, count]
            curr, count = item, 1
    if count > 0:
        yield [curr, count]
def create_list (s_list):
    encoded_list = [pair for pair in encode_list(s_list)]
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]