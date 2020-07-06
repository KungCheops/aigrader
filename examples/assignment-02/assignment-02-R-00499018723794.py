def encode_list(s_list):
    prev_elem = None
    count = 0
    totalcount=0
    n=len(s_list)
    for elem in s_list:
        if elem != prev_elem:
            if prev_elem==None:
                prev_elem=elem
            else:
                yield [prev_elem,count]
                prev_elem=elem
                count=0
        if elem==prev_elem:
            count += 1
        totalcount+=1
        if totalcount==n:
            yield [elem,count]
    return
def create_list (s_list):
    encoded_list=[]
    test=encode_list(s_list)
    for value in test:
        encoded_list.append(value)
    print(encoded_list)
    return encoded_list
if __name__ == "__main__":
    assert (create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]), "Violates Assertion"