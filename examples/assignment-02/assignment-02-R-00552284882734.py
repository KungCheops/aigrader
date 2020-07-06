def encode_list(s_list):
    list_gen = (_ for _ in s_list)
    num_1 = next(list_gen)
    num_2 = next(list_gen)
    counter = 1
    while True:
        while num_1 == num_2:
            counter += 1
            num_2 = next(list_gen)
        gen = yield [num_1, counter]
        num_1 = num_2
        num_2 = next(list_gen, None)
        counter = 1
        if num_2 is None:
            gen = yield [num_1, counter]
            break
    return gen
def create_list(s_list):
    encoded_list = [_ for _ in encode_list(s_list)]
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1, 1, 7, 5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2],
                                                                    [7, 1], [5, 1]]