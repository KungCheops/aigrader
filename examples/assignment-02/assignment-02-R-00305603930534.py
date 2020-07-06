from collections.abc import Iterable
def encode_list(s_list):
    if s_list == None or not isinstance(s_list, Iterable):
        raise Exception('Invalid argument: not iterable')
    counter = 0
    current_encoding_element = s_list[0] if len(s_list) > 0 else None
    for element in s_list:
        if element != current_encoding_element:
            yield [current_encoding_element, counter]
            current_encoding_element = element
            counter = 0
        counter += 1
    if current_encoding_element != None:
        yield [current_encoding_element, counter] 
    return
def create_list (s_list):
    return [encoded_element for encoded_element in encode_list(s_list)]
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]
    assert create_list([]) == []
    assert create_list("") == []
    assert create_list("CAAAAAAGGGT") ==[['C',1], ['A',6], ['G',3], ['T',1]] 