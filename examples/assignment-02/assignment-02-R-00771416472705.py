def encode_list(s_list):
    i = 0
    while (i <= len(s_list) - 1) :
        c = 1
        a = s_list[i]
        j = i + 1
        while (j <= len(s_list) - 1) :
            if a == s_list[j]:
                c = c + 1
                j = j + 1
            else:
                break
        yield [a, c]
        i = j
    return
def create_list (s_list):
    encoded_list=[]
    e_list = encode_list(s_list)
    for x in e_list:
        encoded_list.append(x)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]