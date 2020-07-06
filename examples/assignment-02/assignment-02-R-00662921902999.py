def encode_list(s_list):
    s_old = s_list[0]
    count = 0
    for s in s_list:
        if s == s_old:
            count += 1
        else:
            yield [s_old, count]
            count = 1
        s_old = s
    yield [s_old, count]
def create_list (s_list):
    encoded_list=[x for x in encode_list(s_list)]
    return encoded_list
if __name__ == "__main__":
    print(create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5])) 
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]