def encode_list(s_list):
    current_symbol = None
    count = 0
    for item in s_list:
        if item == current_symbol:
            count += 1
        else:
            if count > 0:
                yield [current_symbol, count]
            current_symbol = item
            count = 1
    yield [current_symbol, count]
    return
def create_list (s_list):
    encoded_list=[]
    encoded_list = [i for i in encode_list(s_list)]
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]