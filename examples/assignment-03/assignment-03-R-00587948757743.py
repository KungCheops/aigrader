def sublist(s_list):
    i = 0 
    u = 0 
    while i < len(s_list):
        yield s_list[u:i+1] 
        elem1 = s_list[i]
        i += 1
        if i < len(s_list): 
            elem2 = s_list[i]
            if elem1 > elem2: 
                while u < i-1:
                    u += 1
                    yield s_list[u:i]
                u += 1
        else:       
            while u < i-1:
                u += 1
                yield s_list[u:i]
    return
def longest_common_list(s_list):
    ordered = [tuple(x) for x in sublist(s_list)]
    reverse = [tuple(x) for x in sublist(list(reversed(s_list)))]
    same_elements = list(set(ordered).intersection(reverse))
    lengths = [len(x) for x in same_elements]
    longest = 0
    argmax = 0
    for i in range(len(lengths)):
        if lengths[i] > longest:
            longest = lengths[i]
            argmax = i
    return list(same_elements[argmax])
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]