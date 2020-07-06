def is_ascending(s_list):
    for i in range(len(s_list)-1):
        if(s_list[i] > s_list[i+1]):
            return False
    return True
def sublist(s_list):
    for i in range(len(s_list)):
        for j in range(i+1, len(s_list)+1):
            if(is_ascending(s_list[i:j])):
                yield s_list[i:j]
    yield []
def longest_common_list(s_list):
    common_sublists = [x for x in sublist(s_list) if x in sublist(s_list[::-1])]
    return max(common_sublists, key=len)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]