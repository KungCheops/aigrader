def encode_list(s_list):
    count, current, n = 0, s_list[0], len(s_list)
    for i in range(n):
        element = s_list[i]
        if element == current:
            count += 1
        else:
            yield [current, count]
            current, count = element, 1
        if i == n-1:
            yield [current, count]
    return
def create_list(s_list):
    encoded_list = []
    gen = encode_list(s_list)
    for item in gen:
        encoded_list.append(item)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1, 1, 7, 5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]