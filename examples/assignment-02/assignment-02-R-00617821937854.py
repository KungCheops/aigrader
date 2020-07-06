def encode_list(s_list):
    count = 1
    prev = None
    for index, value in enumerate(s_list):
        if index == len(s_list)-1:
            yield [s_list[index], count]
            return
        if value == s_list[index+1]:
            count += 1
        else:
            yield [s_list[index], count]
            count = 1
    return
def create_list (s_list):
    encoded_list=[]
    gen = encode_list(s_list)
    encoded_list = list(gen)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]