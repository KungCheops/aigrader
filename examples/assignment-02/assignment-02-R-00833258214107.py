def encode_list(s_list):
    if s_list == []:
        return []
    s_list_iter = iter(s_list)
    prev_value = next(s_list_iter)
    curr_list  = [prev_value]
    for item in s_list_iter:
        if item != prev_value:
            yield curr_list
            curr_list = [item]
        else:
            curr_list.append(item)
        prev_value = item
    yield curr_list
    return
def create_list (s_list):
    encoded_list=[]
    encoded_list = [[x[0], len(x)] for x in encode_list(s_list)]
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]