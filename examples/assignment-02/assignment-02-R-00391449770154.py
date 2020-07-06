def encode_list(s_list):
    c = 1
    for i in range(len(s_list)):
        if i < len(s_list) - 1 and s_list[i] == s_list[i + 1]:
            c += 1
        else:
            yield([s_list[i], c])
            c = 1
    return
def create_list (s_list):
    encoded_list=[]
    return [i for i in encode_list(s_list)] 
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]