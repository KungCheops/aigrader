def encode_list(s_list):
    dataValue = s_list[0]
    count = 0
    for i in s_list:
        if i == dataValue:
            count += 1
        else:
            yield [dataValue, count]
            dataValue = i
            count = 1
    yield [dataValue, count]
def create_list(s_list):
    encoded_list=[]
    encoded_list = [print(dataValue) for dataValue in encode_list(s_list)]
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]