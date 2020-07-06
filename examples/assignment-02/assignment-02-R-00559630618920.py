def encode_list(s_list):
    current = [s_list[0], 0]
    for x in s_list:
        if current[0] != x:
            yield current
            current = [x, 0]
        current[1] += 1
    yield current
def create_list (s_list):
    encoded_list=[]
    for x in encode_list(s_list):
        encoded_list.append(x)
    print(encoded_list)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]