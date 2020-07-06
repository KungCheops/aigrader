def encode_list(s_list):
    i = -1
    while i < len(s_list):
        count = 1
        i += 1
        if i < (len(s_list) - 1):
            while s_list[i] == s_list[i+1]:
                count += 1
                i += 1
        yield [s_list[i], count]
def create_list(s_list):
    encoded_list=[]
    gen = encode_list(s_list)
    while True:
        try:
            encoded_list.append(next(gen))
        except:
            break
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]