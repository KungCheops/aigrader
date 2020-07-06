def encode_list(s_list):
    current_letter = s_list[0]
    counter = 0
    for elem in s_list:
        if elem == current_letter:
            counter += 1
        else:
            yield [current_letter, counter]
            current_letter = elem
            counter = 1
    yield [current_letter, counter]
    return
def create_list (s_list):
    encoded_list=[]
    generator = encode_list(s_list)
    for encoded in generator:
        encoded_list += [encoded]
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]