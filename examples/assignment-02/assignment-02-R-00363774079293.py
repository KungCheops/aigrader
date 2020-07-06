def encode_list(s_list):
    s_old = s_list[0]
    count = 1
    for s in s_list[1:]:
        if s == s_old:
            count += 1
        else:
            yield [s_old, count]
            s_old = s
            count = 1
    if s == s_old:
        yield [s, count]
    else:
        yield [s, 1]
def create_list (s_list):
    encoded_list=[]
    for item in encode_list(s_list):
        encoded_list.append(item)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]