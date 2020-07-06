def encode_list(s_list):
    prev_value = s_list[0]
    cur_value = s_list[1]
    count =  1
    ind = 1
    for i in range(0, len(s_list)):
        ind+=1
        if cur_value == prev_value:
            count +=1
            prev_value = cur_value
            cur_value = s_list[ind]
        else:
            encode_stamp = [prev_value, count]
            count = 1
            yield encode_stamp
            if ind>len(s_list)-1:
               prev_value = cur_value
               cur_value = None
               if cur_value == None and prev_value == None:
                   yield 'generator end'
            else:
                prev_value = cur_value
                cur_value = s_list[ind]
    return 
def create_list (s_list):
    encoded_list=[]
    encode_generator = encode_list(s_list)
    while True:
        n_element = next(encode_generator)
        if n_element == 'generator end':
            break
        encoded_list.append(n_element)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]