def sublist(s_list):
    first, *rest = s_list
    lst = [first]
    for e in rest:
        yield lst
        if e<lst[-1]:
            lst = []
        lst = [*lst, e]
    yield lst
def longest_common_list(s_list):
    return max([l for l in sublist(s_list) if l in sublist(reversed(s_list))], key=len)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]