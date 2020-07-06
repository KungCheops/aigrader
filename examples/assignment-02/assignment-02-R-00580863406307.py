def encode_list(s_list):
    iterator = iter(s_list)
    current_item = next(iterator)
    counter = 1
    for item in iterator:
        if item == current_item:
            counter += 1
        else:
            yield current_item, counter
            current_item = item
            counter = 1
    yield current_item, counter
def create_list (s_list):
    encoded_list=[]
    return [[i,j] for i, j in encode_list(s_list)]
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]
    assert create_list(['C','A','A','A','A','A','A','G','G','G','T']) == [['C', 1], ['A', 6], ['G', 3], ['T', 1]]