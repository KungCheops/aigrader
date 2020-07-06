def encode_list(s_list):
    count = 0
    for i in  range(len(s_list)):
        count += 1
        if i == len(s_list) - 1 or s_list[i] != s_list[i+1]:
            yield [s_list[i], count]
            count = 0
    return
def create_list (s_list):
    gen = encode_list(s_list)
    encoded_list = list(gen)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]