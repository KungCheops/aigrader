def encode_list(s_list):
    lenList = len(s_list)
    nInRow = 1
    counter = 0
    while counter < lenList:
        currElem = s_list[counter]
        if(counter == lenList-1):
            yield [s_list[counter], nInRow]
        elif (currElem == s_list[counter+1]):
            nInRow += 1
        else:
            yield [s_list[counter], nInRow]
            nInRow = 1
        counter += 1
def create_list(s_list):
    encoded_list = list(encode_list(s_list))
    return encoded_list
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1, 1, 7, 5]) == [
        [1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]
    assert create_list('aaaaabbbccc') == [['a', 5], ['b', 3], ['c', 3]]