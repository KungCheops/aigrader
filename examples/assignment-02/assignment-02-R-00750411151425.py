def encode_list(s_list):
    i = 0
    while i < len(s_list):
        current = s_list[i]
        count = 0
        while True:
            if i > len(s_list)-1:
                break
            if s_list[i] == current:
                i += 1
                count += 1
            else:
                break
        yield [current, count]
def create_list (s_list):
    encoded_list=[]
    fn = encode_list(s_list)
    for e in fn:
        encoded_list.append(e)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]