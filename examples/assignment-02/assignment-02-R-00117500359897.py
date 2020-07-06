def encode_list(s_list):
    a = s_list[0]
    b = 0
    for x in s_list:
        if x == a:
            b += 1
        if x != a:
            yield [a, b] 
            a = x
            b = 1
    yield [a, b] 
def create_list(s_list):
    return [i for i in encode_list(s_list)]
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]