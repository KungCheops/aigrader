def encode_list(s_list):
    i = 0
    while i < len(s_list):
        count = 1
        j = i+1
        while j < len(s_list):
            if s_list[i] == s_list[j]:
                count += 1
                j += 1
            else:
                break
        yield [s_list[i], count]
        i = j
    return
def create_list(s_list):
    encoded_list = []
    for i in encode_list(s_list):
        encoded_list.append(i)
    return encoded_list
if __name__ == "__main__":
    encoded_list = create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1, 1, 7, 5])
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]
    print(encoded_list)