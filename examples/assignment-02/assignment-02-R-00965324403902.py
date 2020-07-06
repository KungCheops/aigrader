def encode_list(s_list):
    prev_char = s_list[0]
    count = 1
    if len(s_list) == 1:
        yield [s_list[0], 1]
    for i in range(1, len(s_list)):
        if s_list[i] != prev_char:
            yield [s_list[i-1], count]
            prev_char = s_list[i]
            count = 1
        else:
            count += 1
        if i == len(s_list) - 1:
           yield [s_list[i], count]
def create_list (s_list):
    encoded_list = []
    for e in encode_list(s_list):
        encoded_list.append(e)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]