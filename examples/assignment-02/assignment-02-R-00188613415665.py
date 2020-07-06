def encode_list(s_list):
    return
def create_list (s_list):
    count = 1
    prev = []
    encoded_list = []
    for char in s_list:
        if char != prev:
            if prev:
                entry = [prev,count]
                encoded_list.append(entry)
            count = 1
            prev = char
        else:
            count += 1
    else:
        try:
            entry = [char,count]
            encoded_list.append(entry)
            return encoded_list
        except Exception as e:
            print("Exception {e}".format(e=e))
            return (e, 1)
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]