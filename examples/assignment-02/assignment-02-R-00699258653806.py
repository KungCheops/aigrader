def encode_list(s_list):
    value = s_list[0]
    count = 0
    for s in s_list:
        if s == value:
            count +=1
        else:
            yield [value,count] 
            value = s
            count = 1
    yield [value, count]
def create_list (s_list):
    return [i for i in encode_list(s_list)]
if __name__ == "__main__":
   assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]