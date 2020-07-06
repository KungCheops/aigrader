def encode_list(s_list):
    count = 1
    length = []
    for i in range(1,len(s_list)):
        if s_list[i-1]==s_list[i]:
            count+=1
        else :
            length = [s_list[i-1], count]
            yield length
            count=1
    length = [s_list[i], count]
    yield length
def create_list (s_list):
    encoded_list = []
    encoded_list = [ a for a in encode_list(s_list) if len(s_list)>1]
    print(encoded_list)
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]