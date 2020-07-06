def encode_list(s_list):
    if len(s_list) < 1:         
        return
    prev = [s_list[0], 1]       
    for curr in s_list[1:]:
        if curr != prev[0]:     
            yield prev
            prev = [curr, 1]
        else:                   
            prev[1] += 1
    yield prev
def create_list (s_list):
    encoded_list=[x for x in encode_list(s_list)]
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1, 1, 7, 5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]