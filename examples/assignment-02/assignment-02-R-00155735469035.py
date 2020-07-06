def encode_list(s_list):
    chr=s_list[0]
    n=0
    for c in s_list:
        if c==chr:
            n+=1
        else:
            yield [chr,n]
            n=1
            chr=c
    yield[chr,n]
def create_list (s_list):
    encoded_list=[]
    encodes=encode_list(s_list)
    for encode in encodes:
        encoded_list.append(encode)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]