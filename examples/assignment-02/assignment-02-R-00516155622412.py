def encode_list(s_list):
    count = 1
    c = 0
    while (c != len(s_list)-1):
        a = s_list[c]
        b = s_list[c+1]
        if (a == b):
            c += 1
            count +=1
        else:
            c += 1
            yield([a,count])
            count = 1
    yield([b,count])
def create_list (s_list):
    encoded_list=[]
    gen = encode_list(s_list)
    for i in gen:
        encoded_list.append(i)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]