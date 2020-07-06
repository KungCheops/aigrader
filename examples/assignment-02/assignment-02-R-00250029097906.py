def encode_list(s_list):
    current_count = 1
    for i in range(len(s_list)):
        if i == len(s_list)-1: 
            yield [s_list[i], current_count]
        else:
            if (s_list[i] == s_list[i+1]):
                current_count += 1
            else:
                yield [s_list[i], current_count]
                current_count = 1
def create_list (s_list):
    encoded_list = encode_list(s_list)
    return list(encoded_list)
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2],
                                                [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]