def encode_list(s_list):
    i = 0
    while i <= len(s_list)-1:
        count = 1
        if i == len(s_list)-1:
            yield [s_list[i],count]
            return
        while s_list[i] == s_list[i + 1]:
            count += 1
            i += 1
        yield [s_list[i],count]
        i += 1
def create_list(s_list):
    encoded_list = []
    for j in encode_list(s_list):
        encoded_list.append(j)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]