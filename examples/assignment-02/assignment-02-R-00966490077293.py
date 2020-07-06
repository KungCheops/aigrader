def encode_list(s_list):
    if not s_list:
        return
    current_char = s_list[0]
    counter = 0
    for c in s_list:
        if c == current_char:
            counter += 1
            continue
        yield [current_char, counter]
        current_char = c
        counter = 1
    yield [current_char, counter]
def create_list(s_list):
    encoded_list = []
    encoded_list = [segment for segment in encode_list(s_list)]
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]