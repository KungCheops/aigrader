def encode_list(s_list):
    encoded_list = ''
    previous_s = ''
    s_count = 1
    for s in s_list:
        if s != previous_s:
            if previous_s:
                encoded_list = [previous_s, s_count]
                yield encoded_list
            s_count = 1
            previous_s = s
        else:
            s_count += 1
    encoded_list = [previous_s, s_count]
    yield encoded_list
    return
def create_list (s_list):
    encoded_list=[]
    generator = encode_list(s_list)
    for x in generator:
        encoded_list.append(x)
    return encoded_list
test_list = [1, 1, 1, 2, 3, 3, 4, 4, 5, 1, 1, 7, 5]
new_list = create_list(test_list)
print(new_list)
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]